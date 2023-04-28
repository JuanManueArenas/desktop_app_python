from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Bandera de Francia")

ventana_principal.geometry("500x500")

ventana_principal.config(bg="red")

#---------------------------------
# frame blanco1
#---------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="white" , width=100, height=300)
frame_amarillo.place(x=200, y=100)

#---------------------------------
# frame blanco2
#---------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="white" , width=300, height=100)
frame_amarillo.place(x=100, y=200)




ventana_principal.mainloop()