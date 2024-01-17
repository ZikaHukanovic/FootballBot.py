# Uvozi potrebne biblioteke
import requests
import json

# Definiraj funkciju za dobivanje podataka o igraču
def get_player_info(player_name):
    # Kreiraj URL za upit
    url = "https://www.football-data.org/v2/players/" + player_name

    # Izvuci podatke s URL-a
    response = requests.get(url)
    data = json.loads(response.text)

    # Vrati podatke o igraču
    return data

# Definiraj komande za bota
@client.on("message")
async def on_message(message):
    # Provjeri je li poruka u obliku /ime_igrača
    if message.content.startswith("/"):
        # Izdvoji ime igrača iz poruke
        player_name = message.content[1:]

        # Dobi podatke o igraču
        player_info = get_player_info(player_name)

        # Prikaži podatke o igraču
        await message.channel.send(
            f"Ime: {player_info['name']}\n"
            f"Visina: {player_info['height']}\n"
            f"Broj golova: {player_info['goals']}\n"
            f"Liga: {player_info['league']}\n"
            f"Trofeji: {player_info['trophies']}\n"
        )

# Pokreni bota
client.run("TOKEN")
