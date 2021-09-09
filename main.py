import tkinter as tk
#from signal import pause
#from PIL import ImageTk, Image
import time

window = tk.Tk()
window.title("Hello wold")
window.geometry("300x300")

hello = tk.Label(text="Hello world!")
hello.pack()


def saluda_porllamadoatrasado():
    print('Saludando')


button_adicionar = tk.Button(
    text="Adicionar_T1")  #, command=saluda_porllamadoatrasado)
button_adicionar.pack()
button_sustraer = tk.Button(text="Sustraer_T1",
                            command=saluda_porllamadoatrasado)
button_sustraer.pack()
#button.configure(text = "Goodbye World!", command=goodbye_world)
button_adicionar.configure(command=saluda_porllamadoatrasado)

canvas = tk.Canvas(window, width=800, height=800)
canvas.pack()

img = tk.PhotoImage(file="planta.gif")
canvas.create_image(0, 0, anchor=tk.NW, image=img)


class Tanque:

  
    def __init__(self, capacidad_total, capacidad_inicial, izquierda, abajo,
                 derecha, arriba):
        self.capacidad_total = capacidad_total
        self.capacidad_actual = capacidad_inicial
        self.izquierda = izquierda
        self.abajo = abajo
        self.derecha = derecha
        self.arriba = arriba

        alto = abajo - arriba
        ancho = derecha - izquierda
        altura_liquido = int(alto * self.capacidad_actual /
                             self.capacidad_total)

        self.aire = canvas.create_rectangle(
            izquierda,
            abajo - alto,
            #izquierda+ancho, abajo-alto,
            izquierda + ancho,
            abajo - altura_liquido,
            #izquierda, abajo-altura_liquido,
            fill='white',
            #outline='green',
        )
        self.liquido = canvas.create_rectangle(
            izquierda,
            abajo - altura_liquido,
            #izquierda+ancho, abajo-altura_liquido,
            izquierda + ancho,
            abajo,
            #izquierda, abajo,
            fill='blue',
            #outline='green',
        )

    def dibujo_tkinter(self):
        capacidad_total = self.capacidad_total
        capacidad_actual = self.capacidad_actual
        izquierda = self.izquierda
        abajo = self.abajo
        derecha = self.derecha
        arriba = self.arriba
        alto = abajo - arriba
        ancho = derecha - izquierda
        altura_liquido = int(alto * capacidad_actual / capacidad_total)
        #Dibuja un cuadrado
        canvas.coords(
            self.aire,
            izquierda,
            abajo - alto,
            #izquierda+ancho, abajo-alto,
            izquierda + ancho,
            abajo - altura_liquido,
            #izquierda, abajo-altura_liquido,
        )
        canvas.coords(
            self.liquido,
            izquierda,
            abajo - altura_liquido,
            #izquierda+ancho, abajo-altura_liquido,
            izquierda + ancho,
            abajo,
            #izquierda, abajo,
        )

        return self

    def adicionar(self, cantidad):
        self.capacidad_actual += cantidad
        self.dibujo_tkinter()

    def sustraer(self, cantidad):
        self.adicionar(-cantidad)

    def sustraer10(self):
        self.sustraer(10)

    def adicionar10(self):
        self.adicionar(10)


t1 = Tanque(1000, 800, 65, 142, 184, 37)
t2 = Tanque(1000, 800, 288, 146, 406, 40)
c = Tanque(100, 80, 155, 295, 325, 196)
t3 = Tanque(1000, 800, 295, 452, 488, 353)
button_adicionar.configure(command=c.adicionar10)
button_sustraer.configure(command=c.sustraer10)

tk.mainloop(
)  # El mainloop permite la ejecución de cada callback (llamadoatrasado)
#------------------------------------Ver1

# import tkinter as tk
# #from PIL import ImageTk, Image

# # a continuacion se define el callback (llamadoatrasado) para el boton
# def saluda_porllamadoatrasado():
#   print('Hola')

# window = tk.Tk()
# window.title("Hello wold")
# window.geometry("300x300")

# hello = tk.Label(text="Hello world!")
# hello.pack()
# button = tk.Button(text="Click me!", command=saluda_porllamadoatrasado)
# button.pack()

# canvas=tk.Canvas(window, width=800,height=800)
# canvas.pack()
# img = tk.PhotoImage(file="planta.gif")
# canvas.create_image(0,0,anchor=tk.NW,image=img)

# #Dibuja un cuadrado
# canvas.create_polygon(10, 10,
#                       100, 10,
#                       100, 100,
#                       10, 100,
#                       fill='red',
#                       outline='green')

# #dibuja un triangulo
# canvas.create_polygon(10, 150,
#                       100, 200,
#                       10, 250,
#                       fill='blue',
#                       outline='yellow')

# tk.mainloop()
