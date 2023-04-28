#---------------------------------
# Desktop app No. 1
#---------------------------------

#se importa la libreria tkinter  con todas sus funciones 
from tkinter import *

#-----------------------------
# Funciones de la app
#-----------------------------

#-----------------------------
# Ventana principal app
#-----------------------------

# se declara una variable llaada ventana_principal, que aquiere las caracteristicas de un objeto Tk()

ventana_principal = Tk()

# titulo de la ventana 

ventana_principal.title("Colegio_guanenta")

# tamaño de la ventana 
ventana_principal.geometry("500x500")

# desabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="gray6")

#---------------------------------
# frame amarillo
#---------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="yellow" , width=500, height=500)
frame_amarillo.place(x=0, y=0)

#---------------------------------
# frame azul
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue" , width=500, height=125)
frame_azul.place(x=0, y=250)

#---------------------------------
# frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red" , width=500, height=125)
frame_rojo.place(x=0, y=375)

# run
# se ejecuta  el metodo mainloop() de la clase tk() a travez de la instancia ventana_principa. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acccion del usuario  se conoce 
ventana_principal.mainloop()

