from tkinter import Tk, Entry, Button, Label, OptionMenu, StringVar, messagebox


# -------------------- INTERFAZ --------------------
## Creamos la ventana principal
ventana=Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("420x250")
ventana.config(bg="#239653")  # Fondo
ventana.resizable(0, 0)

# -------------- Titulo de la ventana---------------
titulo=Label(ventana, text="CONVERSOR DE TEMPERATURA", font=("Arial", 16, "bold", "italic", "underline"),bg="#b3fda5", fg="#166337")
titulo.grid(row=3, column=0, columnspan=6, pady=0, padx=6)

# ---------Creamos una variable para guardar la selección del usuario---------------
opcion_origen = StringVar(ventana)
opcion_origen.set("Celsius")  # Valor por defecto

#---------creamos una variable para guardar la selección del usuario a la q vamos a pasar la temperatura---------
opcion_destino = StringVar(ventana)
opcion_destino.set("-")  # Valor por defecto 

# -----------Creamos el menú desplegable con las opciones de temperatura------------
menu_origen = OptionMenu(ventana, opcion_origen, "Celsius", "Fahrenheit", "Kelvin")
menu_origen.config(bg="#f5f5f5", fg="#12773e", font=("Arial", 10), width=12)
menu_origen.grid(row=6, column=0, columnspan=1, padx=1, pady=5)

# -----------Creamos el menú desplegable con las opciones de temperatura----------
menu_destino = OptionMenu(ventana, opcion_destino, "Celsius", "Fahrenheit", "Kelvin")
menu_destino.config(bg="#f5f5f5", fg="#12773e", font=("Arial", 10), width=12)
menu_destino.grid(row=6, column=1, columnspan=1, padx=5, pady=1)

entrada_temp = Entry(ventana, font=("Arial", 12), bg="#f5f5f5", fg="#333333", bd=3, relief="sunken")
entrada_temp.grid(columnspan=1, row=12, column=0, padx=(8,2), pady=5, ipadx=2, ipady=4)



salida_temp=Entry(ventana, font=("Arial", 12), bg="#f5f5f5", fg="#333333", bd=3, relief="sunken")
salida_temp.grid(columnspan=1, row=12, column=1, padx=(2,10),pady=5, ipadx=2, ipady=4)

# -------------------- Función de conversión --------------------
# Esta función se ejecuta al presionar el botón "Convertir"

def convertir():
    try:   # TODO esto está dentro del try
        valor = float(entrada_temp.get())
        origen = opcion_origen.get()
        destino = opcion_destino.get()
# --------------Lógica de conversión------------------
        if origen == destino:
            resultado = valor
        elif origen == "Celsius":
            if destino == "Fahrenheit":
                resultado = valor * 9/5 + 32
            elif destino == "Kelvin":
                resultado = valor + 273.15
        elif origen == "Fahrenheit":
            if destino == "Celsius":
                resultado = (valor - 32) * 5/9
            elif destino == "Kelvin":
                resultado = (valor - 32) * 5/9 + 273.15
        elif origen == "Kelvin":
            if destino == "Celsius":
                resultado = valor - 273.15
            elif destino == "Fahrenheit":
                resultado = (valor - 273.15) * 9/5 + 32

        salida_temp.delete(0, 'end')
        salida_temp.insert(0, round(resultado, 2))

    except ValueError:
        messagebox.showerror("Error", "Debe ingresar solo números")
        salida_temp.delete(0, 'end')
#--------------------- Botón de conversión --------------------
# Creamos el botón que ejecutará la función de conversión

boton_convertir = Button(ventana, text="Convertir", bg="#ff9900", fg="white", command=convertir)
boton_convertir.grid(row=4, column=0, columnspan=2, pady=10)

ventana.mainloop()