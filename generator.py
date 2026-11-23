
import random
from PIL import Image, ImageDraw, ImageFont

def generate_image():
    # Format de l'affiche
    W, H = 900, 1250
    img = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(img)

    # Polices
    try:
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 58)
        info_font = ImageFont.truetype("DejaVuSans.ttf", 42)
        small_font = ImageFont.truetype("DejaVuSans.ttf", 30)
        star_font = ImageFont.truetype("DejaVuSans.ttf", 85)
    except OSError:
        title_font = info_font = small_font = star_font = ImageFont.load_default()

    # En-tête
    draw.text((55, 45), "MINES SIGNAL", fill="#111111", font=title_font)
    draw.text((55, 145), "RANDOM GRID", fill="#2875b8", font=info_font)
    draw.text((55, 225), "Grid: 5 x 5", fill="#222222", font=small_font)
    draw.text((55, 275), "Stars: 4 random positions", fill="#222222", font=small_font)

    # Choisir exactement 4 cases distinctes
    stars = random.sample(range(25), 4)

    # Grille bleue
    cell = 145
    gap = 5
    start_x = 80
    start_y = 390

    for row in range(5):
        for col in range(5):
            index = row * 5 + col

            x = start_x + col * (cell + gap)
            y = start_y + row * (cell + gap)

            x2 = x + cell
            y2 = y + cell

            if index in stars:
                fill = "#ffffff"
                outline = "#2472d8"
            else:
                fill = "#0865ed"
                outline = "#064bb5"

            draw.rounded_rectangle(
                (x, y, x2, y2),
                radius=8,
                fill=fill,
                outline=outline,
                width=5
            )

            if index in stars:
                symbol = "★"
                bbox = draw.textbbox((0, 0), symbol, font=star_font)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]

                draw.text(
                    (
                        x + (cell - tw) / 2,
                        y + (cell - th) / 2 - 12
                    ),
                    symbol,
                    fill="#f5bd35",
                    font=star_font
                )

    # Pied de page
    draw.text(
        (55, 1160),
        "Random positions - Not a game prediction",
        fill="#555555",
        font=small_font
    )

    img.save("mines_signal.png")
    print("Nouvelle grille créée avec exactement 4 étoiles.")

if __name__ == "__main__":
    generate_image()
import random
from PIL import Image, ImageDraw, ImageFont

def generate_image():
    # Format de l'affiche
    W, H = 900, 1250
    img = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(img)

    # Polices
    try:
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 58)
        info_font = ImageFont.truetype("DejaVuSans.ttf", 42)
        small_font = ImageFont.truetype("DejaVuSans.ttf", 30)
        star_font = ImageFont.truetype("DejaVuSans.ttf", 85)
    except OSError:
        title_font = info_font = small_font = star_font = ImageFont.load_default()

    # En-tête
    draw.text((55, 45), "MINES SIGNAL", fill="#111111", font=title_font)
    draw.text((55, 145), "RANDOM GRID", fill="#2875b8", font=info_font)
    draw.text((55, 225), "Grid: 5 x 5", fill="#222222", font=small_font)
    draw.text((55, 275), "Stars: 4 random positions", fill="#222222", font=small_font)

    # Choisir exactement 4 cases distinctes
    stars = random.sample(range(25), 4)

    # Grille bleue
    cell = 145
    gap = 5
    start_x = 80
    start_y = 390

    for row in range(5):
        for col in range(5):
            index = row * 5 + col

            x = start_x + col * (cell + gap)
            y = start_y + row * (cell + gap)

            x2 = x + cell
            y2 = y + cell

            if index in stars:
                fill = "#ffffff"
                outline = "#2472d8"
            else:
                fill = "#0865ed"
                outline = "#064bb5"

            draw.rounded_rectangle(
                (x, y, x2, y2),
                radius=8,
                fill=fill,
                outline=outline,
                width=5
            )

            if index in stars:
                symbol = "★"
                bbox = draw.textbbox((0, 0), symbol, font=star_font)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]

                draw.text(
                    (
                        x + (cell - tw) / 2,
                        y + (cell - th) / 2 - 12
                    ),
                    symbol,
                    fill="#f5bd35",
                    font=star_font
                )

    # Pied de page
    draw.text(
        (55, 1160),
        "Random positions - Not a game prediction",
        fill="#555555",
        font=small_font
    )

    img.save("mines_signal.png")
    print("Nouvelle grille créée avec exactement 4 étoiles.")

if __name__ == "__main__":
    generate_image()
