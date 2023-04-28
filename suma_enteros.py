#---------------------------------
# Desktop app No. 1
#---------------------------------

#se importa la libreria tkinter  con todas sus funciones 
from tkinter import *
from tkinter import messagebox

#-----------------------------
# Funciones de la app
#-----------------------------

# sumar
def sumar():
    pass
# borrar
def borrar():
    pass
# salir
def salir():
    messagebox.showinfo("Suma Enteros 1.0", "la app se va a cerrar")
    ventana_principal.destroy()





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
ventana_principal.config(bg="black")

#---------------------------------
# variables globales 
#---------------------------------
x = StringVar()
y = StringVar()
#---------------------------------
# frame entrada de datos
#---------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white" , width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image = logo, bg = "white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo = Label(frame_entrada, text = "Suma enteros 1.0" )
titulo.config(bg ="white", fg="black", font=("Arial", 16))
titulo.place(x=240, y=10)

# etiqueta para valor de x
lb_x = Label(frame_entrada, text = "X = ")
lb_x.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_x.place(x=240, y=60)

# caja de texto para valor x
entry_x = Entry(frame_entrada, textvariable=X)
entry_x.config(bg="white", fg= "blue", font=("Times New Roman", 18), width=6)
entry_x.focus_set()
entry_x.place(x=290, y=60) 

# etiqueta para valor de y
lb_y = Label(frame_entrada, text = "Y = ")
lb_y.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_y.place(x=240, y=120)

# caja de texto para valor y
entry_y = Entry(frame_entrada, textvariable=Y)
entry_y.config(bg="white", fg= "blue", font=("Times New Roman", 18),width=6)
entry_y.place(x=290, y=120)




#---------------------------------
# frame operaciones 
#---------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white" , width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=sumar)
bt_sumar.place(x=45, y=35, width=100, height=30)

# boton para borrar 
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35,width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=335, y=35,width=100, height=30)

#---------------------------------
# frame resultado
#---------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white" , width=480, height=180)
frame_resultados.place(x=10, y=310)

# area de texto para los resultados 
t_resultados =Text(frame_resultados)
t_resultados.config(bg="black", fg="green2", font=("Courier", 20))
t_resultados.place(x=10, y=10, width=460, height=160)


# run
# se ejecuta  el metodo mainloop() de la clase tk() a travez de la instancia ventana_principa. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acccion del usuario  se conoce 
ventana_principal.mainloop()
