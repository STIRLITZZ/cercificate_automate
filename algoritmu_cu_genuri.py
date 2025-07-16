#pentru codul ista fisierul cu nume trebuie sa fie in format GEN, NUME PRENUME exemplu : M, ANDRANOVICI DUMITRU


from PIL import Image, ImageDraw, ImageFont
import os

list_of_people = []  # va conține tuple: (sex, nume)

def cleanup_data():
    with open('nume.txt', encoding='utf-8') as file:
        for line in file:
            sex, name = line.strip().split(',', 1)
            list_of_people.append((sex.strip().upper(), name.strip()))

def generate_certificates():
    os.makedirs('cerceficat_generat_DOAMNEI', exist_ok=True)
    os.makedirs('cerceficat_generat_DOMNULUI', exist_ok=True)

    for sex, name in list_of_people:
        if sex == 'F':
            template_path = 'Certificat sablon DOAMNEI.png'
            output_dir = 'cerceficat_generat_DOAMNEI'
        elif sex == 'M':
            template_path = 'Certificat sablon DOMNULUI.png'
            output_dir = 'cerceficat_generat_DOMNULUI'
        else:
            print(f"Sex necunoscut pentru: {name}")
            continue

        image = Image.open(template_path).convert('RGB')
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Lora-Bold.ttf", 120)

        bbox = draw.textbbox((0, 0), name.upper(), font=font)
        text_width = bbox[2] - bbox[0]
        image_width = image.size[0]
        x = (image_width - text_width) // 2
        y = 700

        draw.text((x, y), name.upper(), font=font, fill=(0, 0, 0))
        image.save(f'{output_dir}/{name.upper()}.pdf', "PDF", resolution=100.0)

cleanup_data()
generate_certificates()
