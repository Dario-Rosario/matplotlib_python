#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def ej1():
    # Line Plot
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
  

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    x = list(range(-10, 11, 1))
    x2 =np.array(x)

    y1 = x2**2
    y2 = x2**3
    y3 = x2**4 

    gs = gridspec.GridSpec(3, 1)
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[2, 0])

    ax1.plot(x2, y1, color = "b", label = "y1=x**2")
    ax1.set_facecolor("Whitesmoke")
    ax1.set_title("Funcion x cuadrado")
    ax1.set_ylabel("Y")
    ax1.set_xlabel("X")
    ax1.legend()

    ax2.plot(x2, y2, color = "c", label = "y2=x**3")
    ax2.set_facecolor("Whitesmoke")
    ax2.set_title("Funcion x al cubo")
    ax2.set_ylabel("Y")
    ax2.set_xlabel("X")
    ax2.legend()

    ax3.plot(x2, y3, color = "m", label = "y1=x**4")
    ax3.set_facecolor("Whitesmoke")
    ax3.set_title("Funcion x a la cuarta")
    ax3.set_ylabel("Y")
    ax3.set_xlabel("X")
    ax3.legend()

    plt.show()



def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:


    # Realizar dos gráficos que representen
    # y1 = sin(x)
    # y2 = cos(x)
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x

    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.

    x = np.arange(0, 4*np.pi, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    sample_size = 20
    fig = plt.figure()
    fig.suptitle("Grafico de sin y cos", fontsize=14)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    
    ax1.plot(x, y1, color="b", label = "y=sin(x)")
    ax1.set_facecolor("Whitesmoke")

    ax2.plot(x, y2, color="b", label = "y=cos(x)")
    ax2.set_facecolor("Whitesmoke")

    plt.show()


def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]

    fig = plt.figure()
    fig.suptitle("Usos de Lenguajes de Programacion")
    ax = fig.add_subplot()
    ax.bar(lenguajes, performance, label = "lenguajes")
    ax.set_facecolor("Whitesmoke")
    ax.set_ylabel("Performance")
    ax.set_xlabel("Lenguajes de Programacion")
    
    plt.show()


def ej4():
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }

    # El gráfico debe tener usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico

    fig = plt.figure()
    fig.suptitle("Uso de lenguajes de programacion")
    ax = fig.add_subplot()

    ax.pie(uso_lenguajes.values(), labels = uso_lenguajes.keys(), autopct = "%1.1f%%")
    ax.axis("equal")
    plt.show()


def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]

    signal_x = [i for i in signal["X"]]
    signal_y = ["Y" for i in signal]

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(signal_x, signal_y, color = "b")
    ax.set_facecolor("Whitesmoke")
    ax.set_title("Senoidal")

    plt.show()



    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valoresde "X" e "Y" para poder utilizar
    # el line plot y observar la señal

    # signal_x = [....]
    # signal_y = [....]

    # plot(signal_x, signal_y)

    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7

    # filter_signal_x = [....]
    # filter_signal_y = [....]

    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot

    # plot(signal_x, signal_y)
    # scatter(filter_signal_x, filter_signal_y)

    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
