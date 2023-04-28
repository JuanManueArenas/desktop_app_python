from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Bandera de Francia")

ventana_principal.geometry("500x500")

ventana_principal.config(bg="gray6")



#---------------------------------
# frame azul
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue" , width=167, height=500)
frame_azul.place(x=0, y=0)

#---------------------------------
# frame blanco
#---------------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="white" , width=167, height=500)
frame_blanco.place(x=166, y=0)

#---------------------------------
# frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red" , width=167, height=500)
frame_rojo.place(x=333, y=0)

ventana_principal.mainloop()
