from PIL import Image, ImageDraw, ImageFont
import os
from pdf2image import convert_from_path


list_of_names = []

def cleanup_data():
    with open('nume_m.txt', encoding='utf-8') as file:
        for line in file:
            list_of_names.append(line.strip())

def generate_certificates():
    output_dir = 'cerceficat_generat_DOMNULUI'
    os.makedirs(output_dir, exist_ok=True)

    for name in list_of_names:
        image = Image.open('Certificat sablon DOMNULUI.png')
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Lora-Bold.ttf", 120)  # sau "arial.ttf"

        # Obține dimensiunile textului
        bbox = draw.textbbox((0, 0), name.upper(), font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculează poziția pentru centrare
        image_width, image_height = image.size
        x = (image_width - text_width) // 2
        y = 700  # ajustează dacă vrei mai sus/jos

        draw.text((x, y), name.upper(), font=font, fill=(0, 0, 0))

        image.save(f'{output_dir}/{name.upper()}.pdf', "PDF", resolution=100.0)

cleanup_data()
generate_certificates()
