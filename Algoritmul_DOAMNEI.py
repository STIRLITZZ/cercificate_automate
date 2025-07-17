from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import os

list_of_names = []

def cleanup_data():
    with open('nume_f.txt', encoding='utf-8') as file:
        for line in file:
            name = line.strip()
            if name:
                list_of_names.append(name)

def generate_certificates():
    output_dir = 'certificate_generate_DOAMNEI'
    os.makedirs(output_dir, exist_ok=True)

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
