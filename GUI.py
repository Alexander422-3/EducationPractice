import PySimpleGUI as sg
import matplotlib.pyplot as plt
from FuncGUI import draw_figure, getPlot, getResult, ResultCalculate
from Worked import func1, func2, func3

#sg.theme_previewer()
sg.theme("GrayGrayGray")
#sg.theme("DarkBrown3")
functions = {
    '-F1-': func1,
    '-F2-': func2,
    '-F3-': func3
}



layout = [
    [sg.Column([
        #[sg.Text('Выберите f:', font=('Arial Bold', 14), pad=((0, 10), (10, 5))), sg.Combo(list(functions.keys()), key='function', default_value='F1 = 4/X-2*X', readonly=True, text_color='black', font=('Arial Bold', 14), size=(50, 0), enable_events=True)],
        [sg.Button('F1 = 4/X-2*X', key='-F1-', font=('Arial Bold', 14), size=(20, 0), disabled=True),
         sg.Button('F2 = X^3/2 - 5*X', key='-F2-', font=('Arial Bold', 14), size=(20, 0)),
         sg.Button('F3 = -5/X+1.5*X+2', key='-F3-', font=('Arial Bold', 14), size=(20, 0))],
        [sg.Text("Введите а:", font=('Arial Bold', 14), justification='right', pad=((0, 10), (10, 5))), sg.Input('0.25', key="-A-", font=('Arial Bold', 14), size=(50, 0), enable_events=True, justification='left')],
        [sg.Text("Введите b:", font=('Arial Bold', 14), justification='right', pad=((0, 10), (10, 5))), sg.Input('2', key="-B-", font=('Arial Bold', 14), size=(50, 0), enable_events=True, justification='left')],
        [sg.Text("Введите e:", font=('Arial Bold', 14), justification='right', pad=((0, 10), (10, 5))), sg.Input('0.0001', key="-E-", font=('Arial Bold', 14), size=(50, 0), enable_events=True, justification='left')],
        [sg.Button("Вычисление первого шага ", key="-FirstStep-", size=(25, 1), font=('Arial Bold', 14))],
        [sg.Button("Окончательный ответ ", key="-Answer-",  size=(25, 1), font=('Arial Bold', 14))],
        [sg.Text(key="-ERROR-", font=('Arial Bold', 14))],
        [sg.Text(key="-Result-", font=('Arial Bold', 14))],
        [sg.Text(key='-f(x)-', font=('Arial Bold', 14))],
        [sg.Text(key='-Result1-', font=('Arial Bold', 14))],
        [sg.Button('Выход', key='-EXIT-', font=('Arial Bold', 14), size=(20, 0))]
    ], element_justification='left'),
    sg.Column([
        [sg.Canvas(key="-CANVAS-")]
    ], element_justification='left')]
]

window = sg.Window("Комбинированный метод", layout, finalize=True)
fig, ax = plt.subplots()
tkcanvas = draw_figure(fig, window["-CANVAS-"].TKCanvas)
ax.grid()
ax.axhline(y=0, color="black")
ax.axvline(x=0, color="black")
plt.title("Комбинированный метод")
plt.xlabel("X")
plt.ylabel("F(x)")
plt.close()

znach = {"-A-": window["-A-"].get(), "-B-": window["-B-"].get(), "-E-": window["-E-"].get()}
kuroko = {'-F1-': ["0.25", "2", "0.001"], '-F2-': ["2", "6", "0.001"],
          '-F3-': ["0.5", "3", "0.001"]}
test = 0
f1 = "-F1-"
I = 1
while True:
    event, values = window.read()
    if event == "-F1-" or event == "-F2-" or event == "-F3-":
        f1 = event
        I = 1
        for funct in ["-F1-", "-F2-", "-F3-"]:
            window[funct].update(disabled=False)
        window[event].update(disabled=True)
        tkcanvas.get_tk_widget().destroy()
        fig, ax = plt.subplots()
        tkcanvas = draw_figure(fig, window["-CANVAS-"].TKCanvas)
        ax.grid()
        ax.axhline(y=0, color="black")
        ax.axvline(x=0, color="black")
        plt.title("Комбинированный метод")
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.close()
        window["-ERROR-"].update("")
        window["-Result-"].update("")
        window["-Result1-"].update("")
        window["-f(x)-"].Update("")
        window['-A-'].Update(kuroko[f1][0])
        window['-B-'].Update(kuroko[f1][1])
        window['-E-'].Update(kuroko[f1][2])
        window['-FirstStep-'].update("Вычисление первого шага")
        continue
    if event == "-A-" or event == "-B-" or event == "-E-":
        if values[event] == "" or (values[event] == "-" and event != "-E-"):
            znach[event] = values[event]
            window["-FirstStep-"].Update(disabled=True)
            window['-ERROR-'].update("")
            continue
        window["-FirstStep-"].Update(disabled=False)
        window['-ERROR-'].update("")
        try:
            test = float(values[event])
        except Exception:
            window[event].Update(znach[event])
            window['-ERROR-'].update("")
            continue
        if event == "-E-" and test < 0:
            window[event].Update(znach[event])
            window['-ERROR-'].update("")
            continue
        znach[event] = values[event]
        if event == "-E-" and test == 0:
            window["-FirstStep-"].Update(disabled=True)
            window['-ERROR-'].update("")
            continue
        try:
            test = float(znach["-A-"])
            test = float(znach["-B-"])
            test = float(znach["-E-"])
            window["-FirstStep-"].update("Вычисление первого шага")
        except Exception:
            continue
        window["-FirstStep-"].Update(disabled=False)
    if event =='-FirstStep-':
        window['-f(x)-'].update("")
        if window[event].get_text() == "Следующий шаг":
            data = getPlot(I+1, 0)
            tkcanvas.get_tk_widget().destroy()
            tkcanvas = draw_figure(data.gcf(), window["-CANVAS-"].TKCanvas)
            data.close()
            window["-Result-"].Update("Значение x по методу Ньютона = " + str(result[0][I]), font=('Arial Bold', 14))
            window["-f(x)-"].Update("Значение x по методу Хорд = " + str(result[1][I]), font=('Arial Bold', 14))
            window["-Result1-"].update("")
            I += 1
            if len(result[0]) == I or len(result[1]) == I:
                window[event].update("Вычисление первого шага")
                I = 1
            continue
        try:
            a = float(values["-A-"])
            b = float(values["-B-"])
            e = float(values["-E-"])
            f = functions[f1]
        except Exception:
            window["-ERROR-"].Update("Выберите функцию")
        window["-ERROR-"].Update("")
        if f1 in ['-F1-', '-F3-']:
            if float(values['-A-']) == 0:
                window['-ERROR-'].update('Значение переменной "а" не может быть равно нулю', font=('Arial Bold', 14), text_color='red')
                window['-Result-'].update("")
                window['-Result1-'].update("")
                window["-f(x)-"].Update("")
                window["-Answer-"].Update(disabled=True)
                continue
        if f1 in ['-F1-', '-F3-']:
            if float(values['-B-']) == 0:
                window['-ERROR-'].update('Значение переменной "b" не может быть равно нулю', font=('Arial Bold', 14), text_color='red')
                window['-Result-'].update("")
                window['-Result1-'].update("")
                window["-f(x)-"].Update("")
                window["-Answer-"].Update(disabled=True)
                continue
        try:
            ResultCalculate(a, b, e, f)
            data = getPlot(1, 0)
            result = getResult()
        except Exception as error1:
            window["-ERROR-"].Update(error1, font=('Arial Bold', 14), text_color='red')
            window["-Answer-"].Update(disabled=True)
            window['-Result-'].update("")
            window['-Result1-'].update("")
            window["-f(x)-"].Update("")
            continue
        window["-Answer-"].Update(visible=True, disabled=False)
        tkcanvas.get_tk_widget().destroy()
        tkcanvas= draw_figure(data.gcf(), window["-CANVAS-"].TKCanvas)
        window["-Result-"].Update("Значение x по методу Ньютона = " + str(result[0][0]), font=('Arial Bold', 14))
        window["-f(x)-"].update("Значение x по методу Хорд = " + str(result[1][0]), font=('Arial Bold', 14))
        window["-Result1-"].update("")
        if (len(result[0]) >= len(result[1])):
            window["-FirstStep-"].Update("Следующий шаг")
        else:
            window["-FisrtStep-"].Update("Cледующий шаг")
    if event =="-Answer-":
        try:
            a = float(values["-A-"])
            b = float(values["-B-"])
            e = float(values["-E-"])
            f = functions[f1]
        except Exception:
            window["-ERROR-"].Update("Выберите функцию")
        window["-ERROR-"].Update("")
        if f1 in ['-F1-', '-F3-']:
            if float(values['-A-']) == 0:
                window['-ERROR-'].update('Значение переменной "а" не может быть равно нулю', font=('Arial Bold', 14),
                                         text_color='red')
                window['-Result-'].update("")
                window['-Result1-'].update("")
                window["-f(x)-"].Update("")
                window["-Answer-"].Update(disabled=True)
                continue
        if f1 in ['-F1-', '-F3-']:
            if float(values['-B-']) == 0:
                window['-ERROR-'].update('Значение переменной "b" не может быть равно нулю', font=('Arial Bold', 14),
                                         text_color='red')
                window['-Result-'].update("")
                window['-Result1-'].update("")
                window["-f(x)-"].Update("")
                window["-Answer-"].Update(disabled=True)
                continue
        try:
            ResultCalculate(a, b, e, f)
            result = getResult()
        except Exception as error1:
            window["-ERROR-"].Update(error1, font=('Arial Bold', 14), text_color='red')
            window["-Answer-"].Update(disabled=True)
            window['-Result-'].update("")
            window['-Result1-'].update("")
            window["-f(x)-"].Update("")
            continue
        data = getPlot(3, 1)
        tkcanvas.get_tk_widget().destroy()
        tkcanvas = draw_figure(data.gcf(), window["-CANVAS-"].TKCanvas)
        data.close()
        otvet = (result[0][len(result[0])-1]+result[1][len(result[1])-1])/2
        window["-Result-"].Update("X = " + str((result[0][len(result[0])-1]+result[1][len(result[1])-1])/2))
        window["-f(x)-"].Update("F(x)="+str(f(otvet)))
        if(len(result[0])>=len(result[1])):
            window["-Result1-"].Update("Количество итераций = "+str(len(result[0])-1))
        else:
            window["-Result1-"].Update("Количество итераций =" + str(len(result[1]) - 1))
    if event == sg.WINDOW_CLOSED or event =='Exit' or event == '-EXIT-':
        break
window.close()