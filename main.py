"""
@author: Fernando Fdez Martín

"""

import tkinter as tk
from views.home import Home

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Establecemos la ventana en pantalla completa
        self.attributes('-fullscreen', True)

        # Configuramos el título de la ventana
        self.title("Análisis de imágenes")

        # Agregamos un botón de cierre personalizado en la esquina superior izquierda
        close_button = tk.Button(self, text="Cerrar", bg="red", fg="white", command=self.quit)
        close_button.pack(side=tk.RIGHT, anchor=tk.NW)

        # Creamos la pantalla de inicio
        home = Home(self)
        home.pack(fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()
