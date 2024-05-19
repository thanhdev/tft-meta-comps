import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup

FORGE = {
    'Bloodthirster': ['B.F. Sword', 'Negatron Cloak'],
    "Rabadon's Deathcap": ['Needlessly Large Rod', 'Needlessly Large Rod'],
    "Titan's Resolve": ['Chain Vest', 'Recurve Bow'],
    'Ionic Spark': ['Needlessly Large Rod', 'Negatron Cloak'],
    "Guinsoo's Rageblade": ['Recurve Bow', 'Needlessly Large Rod'],
    'Hextech Gunblade': ['B.F. Sword', 'Needlessly Large Rod'],
    'Bramble Vest': ['Chain Vest', 'Chain Vest'],
    'Spear of Shojin': ['B.F. Sword', 'Tear of the Goddess'],
    'Morellonomicon': ['Needlessly Large Rod', 'Giant\'s Belt'],
    'Last Whisper': ['Recurve Bow', 'Sparring Gloves'],
    'Hand of Justice': ['Sparring Gloves', 'Tear of the Goddess'],
    'Giant Slayer': ['B.F. Sword', 'Recurve Bow'],
    'Infinity Edge': ['B.F. Sword', 'Sparring Gloves'],
    "Nashor's Tooth": ['Giant\'s Belt', 'Recurve Bow'],
    'Sunfire Cape': ['Chain Vest', 'Giant\'s Belt'],
    'Edge of Night': ['Chain Vest', 'B.F. Sword'],
    "Archangel's Staff": ['Needlessly Large Rod', 'Tear of the Goddess'],
    "Warmog's Armor": ['Giant\'s Belt', 'Giant\'s Belt'],
    'Jeweled Gauntlet': ['Needlessly Large Rod', 'Sparring Gloves'],
    "Dragon's Claw": ['Negatron Cloak', 'Negatron Cloak'],
    'Blue Buff': ['Tear of the Goddess', 'Tear of the Goddess'],
    'Red Buff': ['Recurve Bow', 'Recurve Bow'],
    'Deathblade': ['B.F. Sword', 'B.F. Sword'],
    'Gargoyle Stoneplate': ['Chain Vest', 'Negatron Cloak'],
    'Crownguard': ['Chain Vest', 'Needlessly Large Rod'],
    'Redemption': ['Giant\'s Belt', 'Tear of the Goddess'],
    'Quicksilver': ['Negatron Cloak', 'Sparring Gloves'],
    'Statikk Shiv': ['Recurve Bow', 'Tear of the Goddess'],
    'Adaptive Helm': ['Negatron Cloak', 'Tear of the Goddess'],
    'Talisman of Speed': [],
    'Talisman of Aid': [],
    'Talisman of Might': [],
    'Tome of Swiftness': [],
    'Scroll of Haste': [],
}


def crawl_team_comps():
    url = 'https://tftactics.gg/tierlist/team-comps/'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    portraits = soup.find_all('div', class_='team-portrait')
    teams = []
    for portrait in portraits:
        team = parse_portrait(portrait)
        calculate_recipes(team)
        teams.append(team)

    path = Path(__file__).parent.parent / 'public' / 'team_comps.json'
    with open(path, 'w') as f:
        json.dump(teams, f, indent=4)
    return teams


def parse_portrait(portrait):
    team = {
        'name': portrait.find('div', class_='team-name-elipsis').contents[
            0].strip(),
        'rank': portrait.find('div', class_='team-rank').text,
        'characters': []
    }
    character_divs = portrait.find('div', class_="team-characters") \
        .find_all('a', class_='characters-item', recursive=False)
    for div in character_divs:
        character = {
            'name': div.find('div', class_='team-character-name').text,
            'avatar': div.find('img')['src'],
            'attrs': div.attrs['class'][1:]
        }
        if images := div.find('div', class_='character-items'):
            character['items'] = [{
                'name': image['alt'],
                'avatar': image['src']
            } for image in images.find_all('img')]
        else:
            character['items'] = []
        team['characters'].append(character)
    return team


def calculate_recipes(team):
    ingredients = {}
    for character in team['characters']:
        for item in character['items']:
            if item['name'] not in FORGE:
                print(f"Item not found: {item['name']}")
                continue
            for ingredient in FORGE[item['name']]:
                ingredients[ingredient] = ingredients.get(ingredient, 0) + 1
    team['ingredients'] = ingredients


if __name__ == '__main__':
    crawl_team_comps()
