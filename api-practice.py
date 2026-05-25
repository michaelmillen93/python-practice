import requests


def get_card(card_name):
    url = f"https://api.scryfall.com/cards/named?exact={card_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        card = response.json()
    except requests.HTTPError as error:
        print(f"{error}")
        return None
    return card


def classify_card(card):
    mana_value = card["cmc"]
    type_line = card["type_line"]

    if "Instant" in type_line or "Sorcery" in type_line:
        return "Interaction / Spell"

    elif mana_value <= 2:
        return "Aggro"

    elif mana_value <= 5:
        return "Midrange"

    else:
        return "Top End"

option = input("Select a card name:")
card = get_card(option)
if card:
    role = classify_card(card)
    print(f"Name: {card['name']}")
    print(f"Mana value: {card['cmc']}")
    print(f"Type: {card['type_line']}")
    print(f"Role: {role}")
else:
    print("Unable to find card data")

