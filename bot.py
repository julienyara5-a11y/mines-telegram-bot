
import os
import requests
import generator

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

def send_signal():
    # Générer l'image et récupérer les positions des étoiles
    stars = generator.generate_image()

    # Construire la grille textuelle 5x5
    rows = []

    for row in range(5):
        line = []

        for col in range(5):
            index = row * 5 + col

            if index in stars:
                line.append("⭐️")
            else:
                line.append("🟦")

        rows.append("".join(line))

    text_grid = "\n".join(rows)

    caption = (
        "🎲 RANDOM SIGNAL\n\n"
        "Bombs: 3 💣\n"
        "Attempts: 3\n\n"
        "👉 Play Here!\n\n"
        f"{text_grid}\n\n"
        "✅ Tutorial\n\n"
        "⚠️ Positions générées aléatoirement, "
        "non garanties."
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    with open("mines_signal.png", "rb") as photo:
        response = requests.post(
            url,
            data={
                "chat_id": CHANNEL_ID,
                "caption": caption
            },
            files={"photo": photo},
            timeout=30
        )

    response.raise_for_status()

    result = response.json()

    if not result.get("ok"):
        raise RuntimeError(result)

    print("Image et grille textuelle envoyées !")

if __name__ == "__main__":
    send_signal()
