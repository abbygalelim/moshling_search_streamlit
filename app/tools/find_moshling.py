import pandas as pd
from tools.constants import DATA, MOSHLINGS_SEED_COMBOS, RARITY_ID, SEED_FILE_DICT


def find_moshling(names: list, printable=False) -> pd.DataFrame:
    ret: dict[str, list] = {'Name': [], 'Set': [], 'Rarity': [], 'Plant 1': [], 'Plant 2': [], 'Plant 3': []}

    for set in DATA:
        set_name = set['name']
        for m in set['moshlings']:
            curr_name = m['name']
            if curr_name in names:
                names.remove(curr_name)
                rarity = RARITY_ID[m['rarityid']] if printable else m['rarityid']

                ret['Name'].append(curr_name)
                ret['Set'].append(set_name)
                ret['Rarity'].append(rarity)

                for i, seed_i in enumerate(['Plant 1', 'Plant 2', 'Plant 3']):
                    seed = MOSHLINGS_SEED_COMBOS[curr_name][i]
                    if printable:
                        if seed in SEED_FILE_DICT:
                            ret[seed_i].append(SEED_FILE_DICT[seed])
                        else:
                            color = seed.split('_')[-1]
                            seed_type = SEED_FILE_DICT['_'.join(seed.split('_')[:-1])]
                            ret[seed_i].append(f'{color[0].upper() + color[1:]} {seed_type}')
                    else:
                        ret[seed_i].append(seed)
                    i += 1

    return pd.DataFrame(ret)
