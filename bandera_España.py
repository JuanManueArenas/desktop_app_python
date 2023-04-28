from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Bandera de España")

ventana_principal.geometry("1000x500")

ventana_principal.config(bg="gray6")

#---------------------------------
# frame amarillo
#---------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="red" , width=1000, height=125)
frame_amarillo.place(x=0, y=0)

#---------------------------------
# frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="yellow" , width=1000, height=250)
frame_rojo.place(x=0, y=125)
                

#---------------------------------
# frame amarillo
#---------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="red" , width=1000, height=125)
frame_amarillo.place(x=0, y=375)
#---------------------------------
# frame amarillo
#---------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="red" , width=100, height=100)
frame_amarillo.place(x=150  , y=200)

ventana_principal.mainloop()




