import tkinter as tk
from tkinter import ttk, messagebox

class ConversionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Unidades")
        
        # Menú principal
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)
        
        conversion_menu = tk.Menu(menu_bar, tearoff=0)
        conversion_menu.add_command(label="Conversión de Longitud", command=self.longitud_window)
        conversion_menu.add_command(label="Conversión de Masa", command=self.masa_window)
        conversion_menu.add_command(label="Conversión de Tiempo", command=self.tiempo_window)
        
        menu_bar.add_cascade(label="Opciones", menu=conversion_menu)

    def longitud_window(self):
        ConversionWindow(self.root, "Longitud", [("Metros", "Kilómetros", 0.001), ("Pulgadas", "Metros", 0.0254)])
        
    def masa_window(self):
        ConversionWindow(self.root, "Masa", [("Kilogramos", "Gramos", 1000), ("Libras", "Kilogramos", 0.453592)])
        
    def tiempo_window(self):
        ConversionWindow(self.root, "Tiempo", [("Segundos", "Minutos", 1/60), ("Horas", "Días", 1/24)])

class ConversionWindow:
    def __init__(self, root, tipo, opciones):
        self.window = tk.Toplevel(root)
        self.window.title(f"Conversión de {tipo}")
        
        tk.Label(self.window, text="Ingrese el valor a convertir:").grid(row=0, column=0, padx=10, pady=10)
        self.input_value = tk.Entry(self.window)
        self.input_value.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.window, text="Seleccione la conversión:").grid(row=1, column=0, padx=10, pady=10)
        self.selected_conversion = ttk.Combobox(self.window, values=[f"{orig} → {dest}" for orig, dest, _ in opciones])
        self.selected_conversion.grid(row=1, column=1, padx=10, pady=10)
        
        self.convert_button = tk.Button(self.window, text="Convertir", command=lambda: self.convert(opciones))
        self.convert_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result_label = tk.Label(self.window, text="Resultado: ")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)
    
    def convert(self, opciones):
        try:
            value = float(self.input_value.get())
            conversion = self.selected_conversion.get()
            for orig, dest, factor in opciones:
                if f"{orig} → {dest}" == conversion:
                    result = value * factor
                    self.result_label.config(text=f"Resultado: {result:.4f} {dest}")
                    return
            messagebox.showerror("Error", "Seleccione una conversión válida")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")

# Inicializar la app
root = tk.Tk()
app = ConversionApp(root)
root.mainloop()