import math
import time
import matplotlib.pyplot as plt
import numpy as np
def func1(x):
    return 4/x-2*x

def func2(x):
    return x ** 3 / 2 - 5 * x #(-4,-2) # (2,6) #(0)

def func3(x):
    return -5/x+1.5*x+2 #(0.5,3) #(-3,-0.75)


def derivative_first(f,x):
    h = 1e-6
    return (f(x+h)-f(x))/h

def derivative_second(f,x):
    h = 1e-6
    return (f(x+h)-2*f(x)+f(x-h))/h**2

def combined_method(a, b, f, e):
    Dot_hord = []
    Dot_newton = []
    Dots = []
    b1 = b
    a1 = a
    if f(a)*f(b) > 0:
        raise ValueError("Ошибка, знаки на концах отрезка должны быть разные")
    x = np.linspace(a, b, 100)
    proiz = derivative_first(f, a)
    if f(a) == 0:
        raise ValueError("График невозможно построить, так как ответ найден сразу, X=" + str(a))
    elif f(b) == 0:
        raise ValueError("График невозможно построить, так как ответ найден сразу, X="+str(b))
    for i in x:
        if derivative_first(f, i)*proiz < 0:
            raise ValueError("На отрезке может быть больше одного корня ")
    if a*b < 0:
        try:
            result = f(0)
        except ZeroDivisionError:
            raise ValueError("Ошибка деления на 0")
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    temp = abs(b - a)
    k = 0
    while(temp > e):
        k += 1
        #if f(a) == 0 or f(b) == 0:
           #break
        if f(a) * derivative_second(f, a) < 0: #Условие начальной точки для метода хорд
            a = a - (((a - b1) * f(a)) / (f(a) - f(b1)))#формулы расчета по методу хорд
            b = b - f(b) / derivative_first(f, b)
            Dot_hord.append(a)
            Dot_newton.append(b)
        elif f(a) * derivative_second(f, a) > 0:#Условие начальной точки для метода касательных
            a = a - f(a) / derivative_first(f, a)#Формулы расчета по методу касательных
            b = b - ((b - a1) * f(b)) / (f(b) - f(a1))
            Dot_hord.append(b)
            Dot_newton.append(a)
        elif f(a)*derivative_second(f, a) == 0:
            raise ValueError("На отрезке больше одного корня")
        temp = abs(b - a)
    if (len(Dot_newton) < 2 or len(Dot_hord) < 2):
       raise ValueError("На данном отрезке невозможно продемонстрировать графически решение"+str((a+b)/2))
    Dots.append(Dot_newton)
    Dots.append(Dot_hord)
    return Dots





#return x ** 3 - 2 * x ** 2 - 19 * x - 20
 #return x**3/2-5*x-2
# result3 = (1,5,0.01)

#return x**3+5*x**2+6*x
# result2 = (-2.5,-1.7,0.01)

#return x**3 + 3*x**2 - 24*x + 1
#result2.3 = 1,5,0.001


# 0,5 2
#-0.2, -2

#return x**3-6*x**2+11*x-6(крутой график(2,5-4)(0,5 - 1.4)
#return x**3 - 7*x**2 + 14*x - 8 #(3,5-5)(-0.5,1.2)(1.55-2.5)


#return x ** 3 / 2 - 5 * x
#return 1/x-1
# return x**3/2-5*x
#b = b - ((a1-b) * f(b)) / (f(a1) - f(b))
#result2 = combined_method(0.5, 5, f, 0.0001) -->3.162
#result1 = combined_method(1, 7, f, 0.0001) --> результат 5.839
#result3 = combined_method(0.5, 5, f, 0.0001) -->2.542