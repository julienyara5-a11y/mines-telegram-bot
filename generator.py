
import random
from PIL import Image, ImageDraw, ImageFont

def generate_image():
    size = 5
    cell = 120
    margin = 20

    width = size * cell + margin * 2
    height = size * cell + margin * 2

    img = Image.new("RGB", (width, height), "#101827")
    draw = ImageDraw.Draw(img)

    stars = random.sample(range(25), 4)

    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 48)
    except OSError:
        font = ImageFont.load_default()

    for row in range(size):
        for col in range(size):
            x1 = margin + col * cell
            y1 = margin + row * cell
            x2 = x1 + cell - 5
            y2 = y1 + cell - 5

            draw.rounded_rectangle(
                (x1, y1, x2, y2),
                radius=12,
                fill="#243449",
                outline="#52677f",
                width=3
            )

            index = row * size + col
            symbol = "★" if index in stars else "?"
            color = "#FFD700" if index in stars else "#FFFFFF"

            bbox = draw.textbbox((0, 0), symbol, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            draw.text(
                (
                    x1 + (cell - text_width) / 2,
                    y1 + (cell - text_height) / 2 - 5
                ),
                symbol,
                fill=color,
                font=font
            )

    img.save("mines_signal.png")
    print("Grille créée avec exactement 4 étoiles.")
