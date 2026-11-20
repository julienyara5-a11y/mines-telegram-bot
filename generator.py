
import random
from PIL import Image, ImageDraw, ImageFont

# Dimensions de la grille
SIZE = 5
CELL = 120
MARGIN = 20

WIDTH = SIZE * CELL + MARGIN * 2
HEIGHT = SIZE * CELL + MARGIN * 2

# Créer l'image
img = Image.new("RGB", (WIDTH, HEIGHT), "#101827")
draw = ImageDraw.Draw(img)

# Choisir exactement 4 cases différentes
positions = random.sample(range(25), 4)

# Dessiner la grille
for row in range(SIZE):
    for col in range(SIZE):
        x1 = MARGIN + col * CELL
        y1 = MARGIN + row * CELL
        x2 = x1 + CELL - 5
        y2 = y1 + CELL - 5

        draw.rounded_rectangle(
            (x1, y1, x2, y2),
            radius=12,
            fill="#243449",
            outline="#52677f",
            width=3
        )

        index = row * SIZE + col

        if index in positions:
            text = "★"
            color = "#FFD700"
        else:
            text = "?"

            color = "#FFFFFF"

        try:
            font = ImageFont.truetype("DejaVuSans.ttf", 48)
        except OSError:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        draw.text(
            (
                x1 + (CELL - text_width) / 2,
                y1 + (CELL - text_height) / 2 - 5
            ),
            text,
            fill=color,
            font=font
        )

img.save("mines_signal.png")
print("Image créée avec exactement 4 étoiles.")
