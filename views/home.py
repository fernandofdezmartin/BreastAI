import tkinter as tk
import cv2
from tkinter import filedialog
import win32api
from PIL import Image, ImageTk


class Home(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.cropped_image_i = None

        self.select_button = tk.Button(self, text="Seleccionar imagen", command=self.select_image,
                               bg="blue", fg="white", relief="raised", padx=10, pady=5)
        self.select_button.pack(side="top", pady=20)
        
        self.image_label = tk.Label(self)
        self.image_label.pack(side="left", padx=30)

        # Inicializar el marco de información de la imagen
        self.image_info_frame = None

    def select_image(self):
        filetypes = (("Archivos de imagen", "*.jpg *.png"), ("Todos los archivos", "*.*"))
        file_path = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=filetypes)
        if file_path:
            image = cv2.imread(file_path)
            height, width, channels = image.shape
            # Leer el tamaño de la pantalla
            if height > 1080 or width > 1920:
                width_screen = win32api.GetSystemMetrics(0)
                height_screen = win32api.GetSystemMetrics(1)
                # Calcular el factor de escala para ajustar el tamaño de la imagen
                factor_escala = min(width_screen/width, height_screen/height)
                # Ajustar el tamaño de la imagen
                image = cv2.resize(image, (int(width * factor_escala), int(height * factor_escala)))
            roi = cv2.selectROI(image,False, False)
            self.cropped_image_i = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
            cv2.destroyAllWindows()
            # Convertir la imagen de OpenCV a formato PIL
            cropped_image = Image.fromarray(self.cropped_image_i)
            # Convertir la imagen de PIL a formato Tkinter
            cropped_image_tk = ImageTk.PhotoImage(cropped_image)
            # Actualizar la etiqueta de imagen en la ventana de Tkinter
            self.image_label.configure(image=cropped_image_tk)
            self.image_label.image = cropped_image_tk
            # Agregar el marco de información de la imagen si no existe
            if self.image_info_frame is None:
                self.image_info_frame = tk.Frame(self)
                self.image_info_frame.pack(side="right", padx=20)
                self.image_info_label = tk.Label(self.image_info_frame, text="Seleccione el tipo de imagen:")
                self.image_info_label.pack(side="left")
                self.mamografia_button = tk.Button(self.image_info_frame, text="Mamografía", command=self.do_mamografia)
                self.mamografia_button.pack(side="left", padx=10)
                self.ultrasonido_button = tk.Button(self.image_info_frame, text="Ultrasonido", command=self.do_ultrasonido)
                self.ultrasonido_button.pack(side="left", padx=10)
            else:
                # Actualizar los botones existentes
                self.mamografia_button.configure(command=self.do_mamografia)
                self.ultrasonido_button.configure(command=self.do_ultrasonido)

    def do_mamografia(self):
        # Ocultamos la pantalla de inicio
        self.pack_forget()

        # Mostramos la pantalla de análisis de imagen
        from views.analysis_m import Analysis_m
        analysis = Analysis_m(self.master, self.cropped_image_i)
        analysis.pack()
        # Hacer algo cuando se selecciona "Mamografía"
        pass

    def do_ultrasonido(self):
        # Hacer algo cuando se selecciona "Ultrasonido"
        self.pack_forget()

        # Mostramos la pantalla de análisis de imagen
        from views.analysis_u import Analysis_u
        analysis = Analysis_u(self.master, self.cropped_image_i)
        analysis.pack()

        pass
