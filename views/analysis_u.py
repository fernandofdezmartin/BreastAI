import tkinter as tk
from PIL import Image, ImageTk
from functions.us import get_result_and_class_us
import cv2
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


class Analysis_u(tk.Frame):
    def __init__(self, master, cropped):
        super().__init__(master)

        result1, img1_array, self.clase = get_result_and_class_us(cropped)

        label_clasificacion = tk.Label(
            self, text="Análisis de imagen", font=("Arial", 19, "bold"))
        label_clasificacion.pack(side="top", padx=120, pady=30)


        self.ultrasonido_button = tk.Button(
            self, text="Generar informe", command=self.generar_pdf)
        self.ultrasonido_button.pack(side="bottom", pady=30)

        texto = tk.Text(self, height=15, width=130)
        texto.insert(tk.END, "Hallazgos: \n\n La mamografía muestra una lesión redondeada bien circunscrita en el cuadrante superior externo de la mama izquierda. La lesión es de alta densidad y tiene bordes espiculados, lo que sugiere la presencia de calcificaciones. Además, se observa distorsión de la arquitectura en la zona circundante de la lesión. La ecografía confirma la presencia de una masa sólida bien circunscrita con bordes espiculados. La lesión mide aproximadamente 2,5 cm y muestra áreas hipoecogénicas en su interior. \n\n Impresión: \n\n Los hallazgos radiológicos son altamente sospechosos de cáncer de mama. La presencia de calcificaciones y bordes espiculados sugiere un tumor maligno. La distorsión de la arquitectura de la mama indica que la lesión puede estar invadiendo los tejidos circundantes. Se recomienda una biopsia para confirmar el diagnóstico y determinar el grado de invasión.")
        texto.pack(side="bottom")

        # Configuramos el widget Label para mostrar la clasificación
        if self.clase == 0:
            clase_texto = "Benigna"
        else:
            clase_texto = "Maligna"

        label_clasificacion = tk.Label(
            self, text=f"Clasificación de lesión: {clase_texto}", font=("Arial", 14, "bold"))
        label_clasificacion.pack(side="bottom", padx=10, pady=30)

        img1_array = cv2.cvtColor(img1_array, cv2.COLOR_BGR2RGB)
        img1_array = Image.fromarray(img1_array)
        img1_array.save("1_u.png")
        result1 = cv2.cvtColor(result1, cv2.COLOR_BGR2RGB)
        result1 = Image.fromarray(result1)
        result1.save("2_u.png")

        # Mostramos la imagen duplicada en un widget Label
        photo = ImageTk.PhotoImage(result1)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack(side='right', expand=True, padx=20)

        photo1 = ImageTk.PhotoImage(img1_array)
        label = tk.Label(self, image=photo1)
        label.image = photo1
        label.pack(side="left", expand=True, padx=20)

    def generar_pdf(self):
        # Create a new PDF document with letter size
        c = canvas.Canvas("informe_u.pdf", pagesize=letter)

        # Draw the title
        c.setFontSize(19)
        c.drawString(120, 750, "Análisis de imagen")

        # Draw the classification label
        c.setFontSize(14)
        if self.clase == 0:
            clase_texto = "Benigna"
        else:
            clase_texto = "Maligna"
        c.drawString(50, 700, f"Clasificación de lesión: {clase_texto}")

        # Load and draw the first image
        img1 = Image.open("1_u.png")
        img1_reader = ImageReader("1_u.png")
        c.drawImage(img1_reader, 50, 450, 250, 250)

        # Load and draw the second image
        img2 = Image.open("2_u.png")
        img2_reader = ImageReader("2_u.png")
        c.drawImage(img2_reader, 300, 450, 250, 250)

        # Draw the button text
        c.setFontSize(12)
        c.drawString(225, 150, "Informe generado con éxito.")

        # Save the PDF document and close the canvas
        c.save()
