import requests

SEED_DICT = {
    '': '',
    'Snap Apple': 'snap_apple',
    'Hot Silly Pepper': 'hot_silly_pepper',
    'Love Berries': 'love_berries',
    'Star Blossom': 'star_blossom',
    'Magic Beans': 'magic_beans',
    'Moon Orchid': 'moon_orchid',
    'Crazy Daisy': 'crazy_daisy',
    'Dragon Fruit': 'dragon_fruit',
}

SEED_FILE_DICT = {
    '': '',
    'snap_apple': 'Snap Apple',
    'hot_silly_pepper': 'Hot Silly Pepper',
    'love_berries': 'Love Berries',
    'star_blossom': 'Star Blossom',
    'magic_beans': 'Magic Beans',
    'moon_orchid': 'Moon Orchid',
    'crazy_daisy': 'Crazy Daisy',
    'dragon_fruit': 'Dragon Fruit',
}

SEED_LIST = list(SEED_DICT.keys())

COLOR_LIST = [
    'any',
    'pink',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple',
    'black',
]

RARITY_ID = {0: 'Ultra Rare', 1: 'Rare', 2: 'Uncommon', 3: 'Common'}

MOSHLING_API = "https://moshionline.net/api?zoo"
DATA = requests.get(MOSHLING_API).json()

SET_AND_MOSHLINGS = {}
MOSHLINGS_SEED_COMBOS: dict[str, list] = {}
MOSHLING_RARITY: dict[int, list] = {}

for set in DATA:
    set_name = set['name']
    set_mosh = []

    for m in set['moshlings']:
        mosh_name = m['name']
        set_mosh.append(mosh_name)

        if m['catchType'] == 'seed':
            seed_combo = []
            for req in m['moshlingRequirements']:
                seed_file = req['path'].split('/')[2].split('.')[0]
                seed_combo.append(seed_file)
        else:
            seed_combo = ['mission', 'mission', 'mission']

        assert len(seed_combo) == 3
        MOSHLINGS_SEED_COMBOS[mosh_name] = seed_combo

        rarity = m['rarityid']
        if rarity in MOSHLING_RARITY:
            MOSHLING_RARITY[rarity].append(mosh_name)
        else:
            MOSHLING_RARITY[rarity] = [mosh_name]

    SET_AND_MOSHLINGS[set_name] = set_mosh
