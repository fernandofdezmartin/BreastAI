# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:08:09 2023

@author: Noemi
"""


# def pdf(ubicacion_mama, Diam_mamo, Vol_mamo, AEfec_mamo, Scoring_mamo, Diam_us, Vol_us, AEfec_us, Scoring_us, seguridad_mamo, seguridad_us):



from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime



# Sacar las magnitudes a través de tamaño de pixel
Diam_mamo=4
Vol_mamo=2.5
AEfec_mamo=16
Scoring_mamo=75
Diam_us=13
Vol_us=5
AEfec_us=22.3
Scoring_us=34
seguridad_mamo=60
seguridad_us=54

ubicacion_mama='DERECHA'
diagnostico_mamo= 'BENIGNO'  #Sacarlo con la seguridad?
diagnostico_us= 'MALIGNO'    #Sacarlo con la seguridad?




doctor='  Fernando Fernández'
paciente=' Noemi Amorós'
nhc='7744321'
birth='28/03/1999'
CP='28521'
fecha = datetime.today().strftime('%Y-%m-%d %H:%M')

cte_vertical=100
cte_horizontal=50




w, h = A4
canvas = canvas.Canvas("Informe_mamo_PPIB.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)

canvas.drawImage('logo.jpg', 30, 680, 75, 75)

canvas.drawString(30,750-cte_vertical,'RESULTADOS DEL ANÁLISIS')
# canvas.drawString(30,735,'HOSPITAL UNIVERSITARIO DE GETAFE')
canvas.drawString(460,750-cte_vertical,str(fecha))
canvas.line(430,747-cte_vertical,580,747-cte_vertical)

canvas.drawString(275,725-cte_vertical,'NHC:')
canvas.drawString(500,725-cte_vertical,str(nhc))
canvas.line(378,723-cte_vertical,580,723-cte_vertical)

canvas.drawString(30,703-cte_vertical,'DOCTOR:')
canvas.line(120,700-cte_vertical,580,700-cte_vertical)
canvas.drawString(120,703-cte_vertical,doctor)


canvas.setFont('Times-Roman', 24)
canvas.drawString(230,670-cte_vertical-20,"Informe mamario")



canvas.line(30, 620-cte_vertical,     580, 620-cte_vertical)
canvas.line(30, 620-cte_vertical-60,  580, 620-cte_vertical-60)
canvas.line(30, 620-cte_vertical,     30,  620-cte_vertical-60)
canvas.line(580,620-cte_vertical,     580, 620-cte_vertical-60)

canvas.setFont('Helvetica', 12)
canvas.drawString(40,620-cte_vertical-20,"Nombre y apellidos:  "+ paciente)
canvas.drawString(40,620-cte_vertical-50,"Fecha de nacimiento:  "+ birth)
canvas.drawString(300,620-cte_vertical-50,"C.I.P:  "+ CP)





canvas.setFont('Helvetica', 12)
canvas.drawString(30,640-2.1*cte_vertical,"Estudio de las imágenes de mamografía:                        "+ ubicacion_mama)
canvas.line(275,636-2.1*cte_vertical,580,636-2.1*cte_vertical)


canvas.line(30+cte_horizontal, 620-30-2.1*cte_vertical, 580, 620-30-2.1*cte_vertical)
canvas.line(30+cte_horizontal, 620-60-2.1*cte_vertical, 580, 620-60-2.1*cte_vertical)
canvas.line(30+cte_horizontal, 620-90-2.1*cte_vertical, 580, 620-90-2.1*cte_vertical)
canvas.line(30+cte_horizontal, 620-120-2.1*cte_vertical, 580, 620-120-2.1*cte_vertical)

canvas.drawString(40+cte_horizontal,620-20-2.1*cte_vertical,"DIAMETRO (mm)")
canvas.drawString(480+cte_horizontal,620-20-2.1*cte_vertical,str(Diam_mamo))

canvas.drawString(40+cte_horizontal,620-50-2.1*cte_vertical,"VOLUMEN (cc)")
canvas.drawString(480+cte_horizontal,620-50-2.1*cte_vertical,str(Vol_mamo))

canvas.drawString(40+cte_horizontal,620-50-30-2.1*cte_vertical,"ÁREA EFECTIVA (mm2)")
canvas.drawString(480+cte_horizontal,620-50-30-2.1*cte_vertical,str(AEfec_mamo))

canvas.drawString(40+cte_horizontal,620-80-30-2.1*cte_vertical,"SCORING")
canvas.drawString(480+cte_horizontal,620-80-30-2.1*cte_vertical,str(Scoring_mamo))

canvas.drawString(40+cte_horizontal,620-110-30-2.1*cte_vertical,"% DE FIABILIDAD")
canvas.drawString(480+cte_horizontal,620-110-30-2.1*cte_vertical,str(seguridad_mamo))


    
canvas.drawImage('mamo.png', 90+cte_horizontal, 220-50-cte_vertical, 150, 150)
canvas.drawImage('mamo_mascara.png', 220+90+cte_horizontal, 220-50-cte_vertical, 150, 150)

canvas.drawString(580,10,"1/4")




##### Cambio de página

canvas.showPage()

canvas.drawImage('logo.jpg', 30, 680, 75, 75)


canvas.drawString(30,750-cte_vertical,'RESULTADOS DEL ANÁLISIS')
# canvas.drawString(30,735,'HOSPITAL UNIVERSITARIO DE GETAFE')
canvas.drawString(460,750-cte_vertical,str(fecha))
canvas.line(430,747-cte_vertical,580,747-cte_vertical)

canvas.drawString(275,725-cte_vertical,'NHC:')
canvas.drawString(500,725-cte_vertical,str(nhc))
canvas.line(378,723-cte_vertical,580,723-cte_vertical)

canvas.drawString(30,703-cte_vertical,'DOCTOR:')
canvas.line(120,700-cte_vertical,580,700-cte_vertical)
canvas.drawString(120,703-cte_vertical,doctor)

canvas.setFont('Helvetica', 12)

canvas.drawString(30,670-cte_vertical-20,"Diagnóstico:         "+ diagnostico_mamo + "  con una seguridad del  " +str(seguridad_mamo) +" %")
canvas.line(120,667-cte_vertical-20,580,667-cte_vertical-20)



canvas.line(30, 670-1.4*cte_vertical,     580, 670-1.4*cte_vertical)
canvas.line(30, 670-1.4*cte_vertical-500,  580, 670-1.4*cte_vertical-500)
canvas.line(30, 670-1.4*cte_vertical,     30,  670-1.4*cte_vertical-500)
canvas.line(580,670-1.4*cte_vertical,     580, 670-1.4*cte_vertical-500)

canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20,"Hallazgos:")   
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-40,"La mamografía realizada a " +paciente+ " reveló los siguientes hallazgos:")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-60," 1. Mama "+ubicacion_mama+":")  

canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-80,"Composición mamaria: La mama "+ubicacion_mama+" muestra una composición predominante")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-100,"grasa/densa.")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-120,"Asimetrías: No se observan asimetrías significativas entre ambas mamas.")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-140,"Calcificaciones: No se identifican calcificaciones sospechosas de malignidad.")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-160,"Nódulos: No se visualizan nódulos ni masas sospechosas en la mama "+ubicacion_mama+".")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-180,"Distorsión arquitectural: No se observa distorsión arquitectural focal.")   

canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-220,"Impresión:")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-240,"El estudio de mamografía realizado a "+paciente+" muestra hallazgos mamográficos ")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-260,"benignos, sin evidencia de anormalizades significativas. No se observan calcificaciones")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-280,"sospechosas de malignidad, nódulos o distorsiones arquitecturales focales.")  

canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-320,"Recomendaciones:") 
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-340,"Dado que los hallazgos mamográficos son benignos, se recomienda seguir con la práctica")   
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-360,"habitual de seguimiento y realizar examenes periódicos según las pautas recomendadas")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-380,"por su médico o especialista. Estos exámenes ayudarán a detectar cualquier cambio ")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-400,"o anormalidad en las mamas.")  

# canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-440,"Línea auxiliar ")  
# canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-460,"Línea auxiliar ")  

canvas.drawString(580,10,"2/4")


##### Cambio de página

canvas.showPage()

canvas.drawImage('logo.jpg', 30, 680, 75, 75)

canvas.drawString(30,750-cte_vertical,'RESULTADOS DEL ANÁLISIS')
canvas.drawString(460,750-cte_vertical,str(fecha))
canvas.line(430,747-cte_vertical,580,747-cte_vertical)

canvas.drawString(275,725-cte_vertical,'NHC:')
canvas.drawString(500,725-cte_vertical,str(nhc))
canvas.line(378,723-cte_vertical,580,723-cte_vertical)

canvas.drawString(30,703-cte_vertical,'DOCTOR:')
canvas.line(120,700-cte_vertical,580,700-cte_vertical)
canvas.drawString(120,703-cte_vertical,doctor)


canvas.setFont('Times-Roman', 24)
canvas.drawString(230,670-cte_vertical-20,"Informe mamario")



canvas.line(30, 620-cte_vertical,     580, 620-cte_vertical)
canvas.line(30, 620-cte_vertical-60,  580, 620-cte_vertical-60)
canvas.line(30, 620-cte_vertical,     30,  620-cte_vertical-60)
canvas.line(580,620-cte_vertical,     580, 620-cte_vertical-60)

canvas.setFont('Helvetica', 12)
canvas.drawString(40,620-cte_vertical-20,"Nombre y apellidos:  "+ paciente)
canvas.drawString(40,620-cte_vertical-50,"Fecha de nacimiento:  "+ birth)
canvas.drawString(300,620-cte_vertical-50,"C.I.P:  "+ CP)



canvas.setFont('Helvetica', 12)
canvas.drawString(30,640-2.1*cte_vertical,"Estudio de las imágenes de ecografía:                        "+ ubicacion_mama)
canvas.line(275,636-2.1*cte_vertical,580,636-2.1*cte_vertical)


canvas.line(30+cte_horizontal, 620-30-2.1*cte_vertical, 580, 620-30-2.1*cte_vertical)
canvas.line(30+cte_horizontal, 620-60-2.1*cte_vertical, 580, 620-60-2.1*cte_vertical)
canvas.line(30+cte_horizontal, 620-90-2.1*cte_vertical, 580, 620-90-2.1*cte_vertical)
canvas.line(30+cte_horizontal, 620-120-2.1*cte_vertical, 580, 620-120-2.1*cte_vertical)

canvas.drawString(40+cte_horizontal,620-20-2.1*cte_vertical,"DIAMETRO (mm)")
canvas.drawString(480+cte_horizontal,620-20-2.1*cte_vertical,str(Diam_us))

canvas.drawString(40+cte_horizontal,620-50-2.1*cte_vertical,"VOLUMEN (cc)")
canvas.drawString(480+cte_horizontal,620-50-2.1*cte_vertical,str(Vol_us))

canvas.drawString(40+cte_horizontal,620-50-30-2.1*cte_vertical,"ÁREA EFECTIVA (mm2)")
canvas.drawString(480+cte_horizontal,620-50-30-2.1*cte_vertical,str(AEfec_us))

canvas.drawString(40+cte_horizontal,620-80-30-2.1*cte_vertical,"SCORING")
canvas.drawString(480+cte_horizontal,620-80-30-2.1*cte_vertical,str(Scoring_us))

canvas.drawString(40+cte_horizontal,620-110-30-2.1*cte_vertical,"% DE FIABILIDAD")
canvas.drawString(480+cte_horizontal,620-110-30-2.1*cte_vertical,str(seguridad_us))


    
canvas.drawImage('us.png', 90+cte_horizontal, 220-50-cte_vertical, 150, 150)
# canvas.drawImage('us.png', 220+90+cte_horizontal, 220-50-cte_vertical, 125, 125)      # Ponerle transparencia
canvas.drawImage('us_mascara.png', 220+90+cte_horizontal, 220-50-cte_vertical, 150, 150)  # Ponerle transparencia

canvas.drawString(580,10,"3/4")


##### Cambio de página

canvas.showPage()

canvas.drawImage('logo.jpg', 30, 680, 75, 75)


canvas.drawString(30,750-cte_vertical,'RESULTADOS DEL ANÁLISIS')
# canvas.drawString(30,735,'HOSPITAL UNIVERSITARIO DE GETAFE')
canvas.drawString(460,750-cte_vertical,str(fecha))
canvas.line(430,747-cte_vertical,580,747-cte_vertical)

canvas.drawString(275,725-cte_vertical,'NHC:')
canvas.drawString(500,725-cte_vertical,str(nhc))
canvas.line(378,723-cte_vertical,580,723-cte_vertical)

canvas.drawString(30,703-cte_vertical,'DOCTOR:')
canvas.line(120,700-cte_vertical,580,700-cte_vertical)
canvas.drawString(120,703-cte_vertical,doctor)


canvas.setFont('Helvetica', 12)

canvas.drawString(30,670-cte_vertical-20,"Diagnóstico:         "+ diagnostico_us + "  con una seguridad del  " +str(seguridad_us) +" %")
canvas.line(120,667-cte_vertical-20,580,667-cte_vertical-20)



canvas.line(30, 670-1.4*cte_vertical,     580, 670-1.4*cte_vertical)
canvas.line(30, 670-1.4*cte_vertical-500,  580, 670-1.4*cte_vertical-500)
canvas.line(30, 670-1.4*cte_vertical,     30,  670-1.4*cte_vertical-500)
canvas.line(580,670-1.4*cte_vertical,     580, 670-1.4*cte_vertical-500)

canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20,"Hallazgos:")   
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-40,"El ultrasonido mamario realizado a " +paciente+ " reveló los siguientes hallazgos:")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-60," 1. Mama "+ubicacion_mama+":")  

canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-80,"Se identifió una lesión focal bien definida en el cuadrante superior externo de la mama, a")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-100,"una profundidad aproximada de [medición en cm].")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-120,"La lesión presenta características ecográficas sospechosas de malignidad, como bordes ")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-140,"irregulares, forma asimétrica y sombras acústicas posteriores.")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-160,"La masa mide aproximadamente "+str(Diam_us)+" en su mayor diámetro.")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-180,"Se observa un patrón interno heterogéneo con áreas de hipoecogenicidad y ecogenicidad")   
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-200,"variable.")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-220,"No se identificario linfodos auxiliares aumentados de tamaño o con características")  
canvas.drawString(55+0.25*cte_horizontal,670-1.4*cte_vertical-20-240,"sospechodas de malignidad.")  

canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-280,"Impresión:")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-300,"Se identificó una masa focal en la mama "+ubicacion_mama+" con características ecográficas sugestivas de")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-320,"malignidad. Los halalzgos son consistentes con un posible tumor maligno. Se recomienda realizar") 
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-340,"estudios adicionales para confirmar el diagnóstico, como una biopsia por punción con aguja fina")   
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-360,"(BAAF) o una biopsia por escisión")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-400,"Es importante tener en cuenta que este informe describe únicamente los hallazgos ecográficos y")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-420,"no constituye un diagnóstico definitivo. La evaluación clínica integral y los estudios adicionales son")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-440,"necesarios para establecer un diagnóstico y un plan de tratamiento adecuados. Se recomienda ")  
canvas.drawString(35+0.25*cte_horizontal,670-1.4*cte_vertical-20-460,"discutir estos resultados con el médico solicitante para una adecuada interpretación y seguimiento.")  

canvas.drawString(580,10,"4/4")

canvas.save()