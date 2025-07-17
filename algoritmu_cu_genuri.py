#pentru codul ista fisierul cu nume trebuie sa fie in format GEN, NUME PRENUME exemplu : M, ANDRANOVICI DUMITRU


from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import os

list_of_names = []  # va conține tuple: (sex, nume)

def cleanup_data():
    with open('nume.txt', encoding='utf-8') as file:
        for line in file:
            sex, name = line.strip().split(',', 1)
            list_of_names.append((sex.strip().upper(), name.strip()))

def generate_certificates():
    os.makedirs('cerceficat_generat_DOAMNEI', exist_ok=True)
    os.makedirs('cerceficat_generat_DOMNULUI', exist_ok=True)

    for sex, name in list_of_names:
        if sex == 'F':
            template_path = 'Certificat sablon DOAMNEI.png'
            output_dir = 'cerceficat_generat_DOAMNEI'
        elif sex == 'M':
            template_path = 'Certificat sablon DOMNULUI.png'
            output_dir = 'cerceficat_generat_DOMNULUI'
        else:
            print(f"Sex necunoscut pentru: {name}")
            continue

        pdfmetrics.registerFont(TTFont('LoraBold', 'Lora-Bold.ttf'))  # înlocuiește cu 'arial.ttf' dacă e cazul

        image_path = 'Certificat sablon DOAMNEI.png'
        background = ImageReader(image_path)

        # Află dimensiunea imaginii
        image = Image.open(image_path)
        page_width, page_height = image.size  # 2000 x 1414

        for name in list_of_names:
            filename = os.path.join(output_dir, f"{name.upper()}.pdf")
            c = canvas.Canvas(filename, pagesize=(page_width, page_height))

            # Fundalul
            c.drawImage(background, 0, 0, width=page_width, height=page_height)

            # Scrierea numelui centrat
            font_size = 90
            c.setFont("LoraBold", font_size)
            text_width = pdfmetrics.stringWidth(name.upper(), "LoraBold", font_size)
            x = (page_width - text_width) / 2
            y = 600  # poziția verticală — o poți ajusta

            c.drawString(x, y, name.upper())
            c.save()


cleanup_data()
generate_certificates()
