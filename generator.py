
import random
from PIL import Image, ImageDraw, ImageFont

def generate_image():
    W, H = 900, 1200
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    try:
        title = ImageFont.truetype("DejaVuSans-Bold.ttf", 54)
        info = ImageFont.truetype("DejaVuSans.ttf", 42)
        play = ImageFont.truetype("DejaVuSans-Bold.ttf", 48)
        star_font = ImageFont.truetype("DejaVuSans.ttf", 75)
        footer = ImageFont.truetype("DejaVuSans.ttf", 25)
    except OSError:
        title = info = play = star_font = footer = ImageFont.load_default()

    # En-tête
    draw.text((45, 35), "RANDOM SIGNAL", fill="#111111", font=title)

    draw.text((45, 130), "Bombs: 3", fill="#222222", font=info)
    draw.text((45, 195), "Attempts: 3", fill="#222222", font=info)

    draw.text((45, 290), "Play Here!", fill="#2875b8", font=play)

    # Sélection de 4 positions aléatoires
    stars = random.sample(range(25), 4)

    # Grille 5 x 5
    cell = 130
    gap = 5
    start_x = 112
    start_y = 390

    for row in range(5):
        for col in range(5):
            index = row * 5 + col

            x = start_x + col * (cell + gap)
            y = start_y + row * (cell + gap)

            if index in stars:
                fill = "#ffffff"
                outline = "#2472d8"
            else:
                fill = "#0865ed"
                outline = "#064bb5"

            draw.rounded_rectangle(
                (x, y, x + cell, y + cell),
                radius=5,
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
                        y + (cell - th) / 2 - 10
                    ),
                    symbol,
                    fill="#f5bd35",
                    font=star_font
                )

    draw.text(
        (45, 1090),
        "Random positions - Not a game prediction",
        fill="#555555",
        font=footer
    )

    img.save("mines_signal.png")
    print("Grille créée avec exactement 4 étoiles.")

if __name__ == "__main__":
    generate_image()return stars
