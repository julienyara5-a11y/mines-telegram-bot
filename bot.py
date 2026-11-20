
import os
import requests
import generator

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

def send_signal():
    generator.generate_image()

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    with open("mines_signal.png", "rb") as photo:
        response = requests.post(
            url,
            data={
                "chat_id": CHANNEL_ID,
                "caption": (
                    "💣 MINES SIGNAL\n\n"
                    "⭐ Grille 5x5 avec exactement 4 étoiles\n"
                    "🎲 Positions générées aléatoirement\n"
                    "⚠️ Ceci n'est pas une prédiction du jeu."
                )
            },
            files={"photo": photo},
            timeout=30
        )

    response.raise_for_status()
    print("Signal envoyé avec succès !")

if __name__ == "__main__":
    send_signal()
