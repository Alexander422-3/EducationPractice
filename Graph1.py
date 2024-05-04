import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from Worked import func1, func2, func3, combined_method, derivative_second
import time


fig, ax = plt.subplots()
ax.grid()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
e = float(input("Введите значение e: "))
choice = int(input("Введите функцию, которую хотите выбрать: "))

if choice == 1:
    f = func1
    if (a == 0 or b == 0) or (a*b < 0):
        print("Функция не вычисляется в этой точке")
        exit(1)
elif choice == 2:
    f = func2
elif choice == 3:
    f = func3
    if (a == 0 or b == 0) or (a*b < 0):
        print("Функция не вычисляется в этой точке")
        exit(1)
else:
    print("Вы ввели некорректный номер")
    exit(1)

result = combined_method(a, b, f, e)


ax.axvline(x=a, color="black")
ax.axvline(x=b, color="black")


x = np.linspace(a, b, 10000)
y = f(x)



#Метод Ньютона
if f(a)*derivative_second(f, a) < 0:
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


i=0
j=0

def update(frame):
    if time.time()-start_time>1:
        legend_shown =False
        # Ньютон
        global x_start, x_end, y_start, y_end, i
        # Хорд
        global x_start1, x_end1, y_start1, y_end1, j
        # Ньютон
        x = [x_start, x_end]
        y = [y_start, y_end]
        # Хорд
        x1 = [x_start1, x_end1]
        y1 = [y_start1, y_end1]
        # Ньютон
        ax.plot(x, y, color="red", label="Ньютон")
        ax.text(x_start, y_end, "x"+str(i), fontsize="large")
        #ax.text(x_end, y_end, "x"+str(i), fontsize="large")
        # Хорд
        ax.plot(x1, y1, color="orange", label="Хорд")
        ax.text(x_start1, 0, "x'" + str(j), fontsize="large")
        if i+1 == 4 and j+1 == 4:
            ani.event_source.stop()
            return
        if not legend_shown:
            ax.legend()
            legend_shown = True
        #Ньютон
        x_start = result[0][i]
        x_end = result[0][i+1]
        y_start = f(result[0][i])
        y_end = 0
        i += 1
        #Хорд
        x_start1 = result[1][j]
        y_start1 = f(result[1][j])
        j += 1

start_time=time.time()

ani = FuncAnimation(fig, update, frames=300, interval=1000)

ax.set_title('Комбинированный метод')
plt.xlabel("X")
plt.ylabel("F(X)")
plt.plot(x, y)
plt.show()




#Ньютон
#line, = ax.plot([], [], color='red')

#Для следующей точки Ньютона
#x_start,x_end = result[0][0], result[0][1]
#y_start,y_end = f(result[0][0]), 0



#][ord

#Метод Хорд
#x_start1, x_end1 = a, b
#y_start1, y_end1 = f(a), f(b)



#Для следующей точки Хорд
#x_start,x_end = result[1][j], b
#y_start,y_end = f(result[1][j]), f(b)
    #x1 = [x_start1, x_start1 + (x_end1 - x_start1) * frame / 100]
    #y1 = [y_start1, y_start1 + (y_end1 - y_start1) * frame / 100]
    #line1.set_data(x1, y1)
    #if x1[1] >= b:
       # ani1.event_source.stop()
    #return line1,