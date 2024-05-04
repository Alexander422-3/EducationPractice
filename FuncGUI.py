from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import numpy as np
from Worked import func1, func2, func3, combined_method, derivative_second
import matplotlib.pyplot as plt
import time

def draw_figure(figure,canvas):
    tkcanvas = FigureCanvasTkAgg(figure, canvas)
    tkcanvas.draw()
    tkcanvas.get_tk_widget().pack(side="top", fill="both", expand=1)
    return tkcanvas

def getPlot(Iteration, FLAG):
    global iteratsiya
    global result
    global a,b,e,f
    global x_start, x_end, y_start, y_end, i
    global x_start1, x_end1, y_start1, y_end1, j
    fig, ax = plt.subplots()
    iteratsiya = Iteration
    ax.grid()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.axvline(x=a, color="black")
    ax.axvline(x=b, color="black")
    plt.xlim(a-abs(b-a)/10, b+abs(b-a)/10)
    x = np.linspace(a, b, 10000)
    y = f(x)
    ax.plot(x, y)
    # Метод Ньютона
    if f(a) * derivative_second(f, a) < 0:
        x_start, x_end = b, result[0][0]
        y_start, y_end = f(b), 0
    elif f(a) * derivative_second(f, a) > 0:
        x_start, x_end = a, result[0][0]
        y_start, y_end = f(a), 0

    if f(a) * derivative_second(f, a) < 0:  # Условие начальной точки для метода хорд
        x_start1, x_end1 = a, b
        y_start1, y_end1 = f(a), f(b)
    elif f(a) * derivative_second(f, a) > 0:
        x_start1, x_end1 = b, a
        y_start1, y_end1 = f(b), f(a)

    i = 0
    j = 0
    legend_shown = False
    for u in range(Iteration):
        # Ньютон
        x = [x_start, x_end]
        y = [y_start, y_end]
        # Хорд
        x1 = [x_start1, x_end1]
        y1 = [y_start1, y_end1]
        # Ньютон
        ax.plot(x, y, color="red", label="Ньютон")
        ax.text(x_start, y_end, "x" + str(i), fontsize="large")
        # Хорд
        ax.plot(x1, y1, color="orange", label="Хорд")
        ax.text(x_start1, 0, "x'" + str(j), fontsize="large")
        if not legend_shown:
            ax.legend()
            legend_shown = True
        try:
            # Ньютон
            x_start = result[0][i]
            x_end = result[0][i + 1]
            y_start = f(result[0][i])
            y_end = 0
            i += 1
            # Хорд
            x_start1 = result[1][j]
            y_start1 = f(result[1][j])
            j += 1
        except Exception:
            break
    ax.set_title('Комбинированный метод')
    plt.xlabel("X")
    plt.ylabel("F(X)")
    if FLAG == 1:
        ax.plot((result[0][len(result[0])-1]+result[1][len(result[1])-1])/2, 0, ':o', color="green", label='X')
    #plt.plot(x, y)
    return plt

def getResult():
    global result
    return result


def ResultCalculate(a1, b1, e1, choice):
    global result
    result = combined_method(a1, b1, choice, e1)
    global a, b, e, f
    a = a1
    b = b1
    e = e1
    f = choice
