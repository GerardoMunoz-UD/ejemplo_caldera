import tkinter as tk
#from PIL import ImageTk, Image


# a continuacion se define el callback (llamadoatrasado) para el boton
def saluda_porllamadoatrasado():
  print('Hola')

window = tk.Tk()
window.title("Hello wold")
window.geometry("300x300")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!", command=saluda_porllamadoatrasado)
button.pack()

canvas=tk.Canvas(window, width=800,height=800)
canvas.pack()
img = tk.PhotoImage(file="planta.gif")
canvas.create_image(0,0,anchor=tk.NW,image=img)

#Dibuja un cuadrado
canvas.create_polygon(10, 10,
                      100, 10,
                      100, 100,
                      10, 100,
                      fill='red',
                      outline='green')

#dibuja un triangulo
canvas.create_polygon(10, 150,
                      100, 200,
                      10, 250,
                      fill='blue',
                      outline='yellow')
