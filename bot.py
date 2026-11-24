import os
import random
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

def send_signal():
    # Choisir exactement 4 positions aléatoires
    stars = random.sample(range(25), 4)

    # Construire la grille sans espaces
    rows = []

    for row in range(5):
        line = ""

        for col in range(5):
            index = row * 5 + col

            if index in stars:
                line += "⭐️"
            else:
                line += "🟦"

        rows.append(line)

    grid = "\n".join(rows)

    # Remplacez ces liens par les vôtres
    play_url = "https://lkuf.cc/321d3b"
    tutorial_url = "https://t.me/votre_lien_tutoriel"

    message = (
        "✅ CONFIRMED ENTRY\n\n"
        "Bombs: 3 💣\n"
        "Attempts: 3\n\n"
        f"👉 [Play Here!]({play_url})\n\n"
        f"{grid}\n\n"
        f"✅ [Tutorial]({tutorial_url})"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHANNEL_ID,
            "text": message,
            "parse_mode": "Markdown"  # Indispensable pour activer les liens cliquables
        },
        timeout=30
    )

    response.raise_for_status()
    print("Signal texte envoyé avec succès !")

if __name__ == "__main__":
    send_signal()
