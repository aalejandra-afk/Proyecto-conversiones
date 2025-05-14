import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Validación de número
def validar_numero(valor):
    try:
        return float(valor)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")
        return None

# Longitud
def convertir_longitud():
    ventana = tk.Toplevel()
    ventana.title("Conversión de Longitud")
    ventana.geometry("300x230")
    ventana.configure(bg="#dceeff")  # azul suave

    opciones = ["Metros a Kilómetros", "Pulgadas a Metros"]

    tk.Label(ventana, text="Valor a convertir:", bg="#dceeff", font=("Arial", 10)).pack(pady=5)
    entrada = tk.Entry(ventana)
    entrada.pack(pady=5)

    combo = ttk.Combobox(ventana, values=opciones, state="readonly")
    combo.current(0)
    combo.pack(pady=5)

    resultado = tk.Label(ventana, text="Resultado:", bg="#dceeff", fg="#6a0dad", font=("Arial", 12))
    resultado.pack(pady=5)

    def convertir():
        valor = validar_numero(entrada.get())
        if valor is not None:
            if combo.get() == "Metros a Kilómetros":
                res = valor / 1000
                resultado.config(text=f"{res:.3f} km")
            elif combo.get() == "Pulgadas a Metros":
                res = valor * 0.0254
                resultado.config(text=f"{res:.3f} m")

    tk.Button(ventana, text="Convertir", bg="#a084dc", fg="white", command=convertir).pack(pady=10)

# Masa
def convertir_masa():
    ventana = tk.Toplevel()
    ventana.title("Conversión de Masa")
    ventana.geometry("300x230")
    ventana.configure(bg="#dceeff")

    opciones = ["Kilogramos a Gramos", "Libras a Kilogramos"]

    tk.Label(ventana, text="Valor a convertir:", bg="#dceeff", font=("Arial", 10)).pack(pady=5)
    entrada = tk.Entry(ventana)
    entrada.pack(pady=5)

    combo = ttk.Combobox(ventana, values=opciones, state="readonly")
    combo.current(0)
    combo.pack(pady=5)

    resultado = tk.Label(ventana, text="Resultado:", bg="#dceeff", fg="#6a0dad", font=("Arial", 12))
    resultado.pack(pady=5)

    def convertir():
        valor = validar_numero(entrada.get())
        if valor is not None:
            if combo.get() == "Kilogramos a Gramos":
                res = valor * 1000
                resultado.config(text=f"{res:.2f} g")
            elif combo.get() == "Libras a Kilogramos":
                res = valor * 0.453592
                resultado.config(text=f"{res:.3f} kg")

    tk.Button(ventana, text="Convertir", bg="#a084dc", fg="white", command=convertir).pack(pady=10)

# Tiempo
def convertir_tiempo():
    ventana = tk.Toplevel()
    ventana.title("Conversión de Tiempo")
    ventana.geometry("300x230")
    ventana.configure(bg="#dceeff")

    opciones = ["Segundos a Minutos", "Horas a Días"]

    tk.Label(ventana, text="Valor a convertir:", bg="#dceeff", font=("Arial", 10)).pack(pady=5)
    entrada = tk.Entry(ventana)
    entrada.pack(pady=5)

    combo = ttk.Combobox(ventana, values=opciones, state="readonly")
    combo.current(0)
    combo.pack(pady=5)

    resultado = tk.Label(ventana, text="Resultado:", bg="#dceeff", fg="#6a0dad", font=("Arial", 12))
    resultado.pack(pady=5)

    def convertir():
        valor = validar_numero(entrada.get())
        if valor is not None:
            if combo.get() == "Segundos a Minutos":
                res = valor / 60
                resultado.config(text=f"{res:.2f} min")
            elif combo.get() == "Horas a Días":
                res = valor / 24
                resultado.config(text=f"{res:.2f} días")

    tk.Button(ventana, text="Convertir", bg="#a084dc", fg="white", command=convertir).pack(pady=10)

# VENTANA PRINCIPAL
root = tk.Tk()
root.title("Menú de Conversiones")
root.geometry("350x350")
root.configure(bg="#b8c6ff")  # fondo azul pastel

tk.Label(root, text="Selecciona un tipo de conversión:", font=("Arial", 14), bg="#b8c6ff", fg="#4b0082").pack(pady=20)

tk.Button(root, text="Conversión de Longitud", width=25, bg="#a084dc", fg="white", font=("Arial", 10), command=convertir_longitud).pack(pady=10)
tk.Button(root, text="Conversión de Masa", width=25, bg="#a084dc", fg="white", font=("Arial", 10), command=convertir_masa).pack(pady=10)
tk.Button(root, text="Conversión de Tiempo", width=25, bg="#a084dc", fg="white", font=("Arial", 10), command=convertir_tiempo).pack(pady=10)

root.mainloop()
