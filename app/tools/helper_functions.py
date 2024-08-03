import pandas as pd
import streamlit as st
from tools.constants import DATA, GARDEN_PATH, MOSHLING_LIST, MOSHLINGS_SEED_COMBOS, RARITY_ID, SEED_FILE_DICT


def create_header(header: str, subheader: str = ''):
    st.header(header, divider='rainbow')
    if subheader:
        st.markdown(f'<p style="font-size: 20px"> {subheader} </p>', unsafe_allow_html=True)


def get_moshling_index(name: str):
    assert len(MOSHLING_LIST) == len(MOSHLINGS_SEED_COMBOS), 'New moshlings added, update garden.csv'

    return MOSHLING_LIST.index(name)


def get_owned(name: str):
    garden_data = pd.read_csv(GARDEN_PATH)
    return garden_data.loc[get_moshling_index(name), 'Owned']


def get_moshling_info(names: list, printable=False) -> pd.DataFrame:
    names = names.copy()

    ret: dict[str, list[str]] = {
        'Name': [],
        'Set': [],
        'Owned': [],
        'Rarity': [],
        'Color 1': [],
        'Plant 1': [],
        'Color 2': [],
        'Plant 2': [],
        'Color 3': [],
        'Plant 3': [],
    }

    for set in DATA:
        set_name = set['name']
        for m in set['moshlings']:
            curr_name = m['name']
            if curr_name in names:
                names.remove(curr_name)
                rarity = RARITY_ID[m['rarityid']] if printable else m['rarityid']

                ret['Name'].append(curr_name)
                ret['Set'].append(set_name)
                ret['Owned'].append(get_owned(curr_name))
                ret['Rarity'].append(rarity)

                color_i = ['Color 1', 'Color 2', 'Color 3']
                plant_i = ['Plant 1', 'Plant 2', 'Plant 3']
                for i, curr_plant in enumerate(plant_i):
                    seed = MOSHLINGS_SEED_COMBOS[curr_name][i]
                    if printable:
                        if seed in SEED_FILE_DICT:
                            ret[color_i[i]].append('any')
                            ret[curr_plant].append(SEED_FILE_DICT[seed])
                        else:
                            color = seed.split('_')[-1]
                            ret[color_i[i]].append(color)
                            seed_type = SEED_FILE_DICT['_'.join(seed.split('_')[:-1])]
                            ret[curr_plant].append(seed_type)
                    else:
                        ret[curr_plant].append(seed)
                    i += 1

    return pd.DataFrame(ret)
