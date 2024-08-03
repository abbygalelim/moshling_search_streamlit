from itertools import combinations_with_replacement

import pandas as pd
import streamlit as st
from tools.constants import COLOR_LIST, POUCH_PATH, SEED_DICT, SEED_FILE_DICT, SEED_LIST
from tools.helper_functions import create_header, get_moshling_info, get_owned
from tools.seed_search import search_moshling_by_seed


def moshling_see_combo_search():
    create_header(
        'Moshling Seed Combo Search',
        'Select any number of seeds and colors to find out which moshlings are attracted to that combination.',
    )

    type_of_results = st.selectbox("Type of results", options=["General", "Specific"])

    col_1, col_2, col_3 = st.columns(3)
    # You can use a column just like st.sidebar:
    with col_1:
        c1 = st.selectbox("Color 1", options=COLOR_LIST)
        s1 = st.selectbox("Seed 1", options=SEED_LIST)
    with col_2:
        c2 = st.selectbox("Color 2", options=COLOR_LIST)
        s2 = st.selectbox("Seed 2", options=SEED_LIST)
    with col_3:
        c3 = st.selectbox("Color 3", options=COLOR_LIST)
        s3 = st.selectbox("Seed 3", options=SEED_LIST)

    selected_combo = []
    if s1:
        if c1 != 'any':
            selected_combo.append(f'{SEED_DICT[s1]}_{c1}')
        else:
            selected_combo.append(SEED_DICT[s1])
    if s2:
        if c2 != 'any':
            selected_combo.append(f'{SEED_DICT[s2]}_{c2}')
        else:
            selected_combo.append(SEED_DICT[s2])
    if s3:
        if c3 != 'any':
            selected_combo.append(f'{SEED_DICT[s3]}_{c3}')
        else:
            selected_combo.append(SEED_DICT[s3])

    mosh_results = []
    if selected_combo:
        mosh_results = search_moshling_by_seed(selected_combo, type_of_results)

    output = get_moshling_info(mosh_results, printable=True)

    st.dataframe(output, use_container_width=True)


def num_mosh_every_combo():
    unique_combos: list[tuple] = list(combinations_with_replacement(list(SEED_FILE_DICT.keys())[1:], 3))
    ret: dict[str, list] = {
        'Seed Combos': [],
        'Not Owned': [],
        'All Possible Moshlings': [],
    }

    for combo in unique_combos:
        combo = list(combo)
        matches = search_moshling_by_seed(combo)
        not_owned_count = 0
        for name in matches:
            if get_owned(name) == 'No':
                not_owned_count += 1

        combo_str = []
        for seed in combo:
            combo_str.append(SEED_FILE_DICT[seed])

        ret["Seed Combos"].append(' / '.join(sorted(combo_str)))
        ret["Not Owned"].append(not_owned_count)
        ret["All Possible Moshlings"].append(len(matches))

    st.subheader('All Combinations', divider='blue')
    st.dataframe(pd.DataFrame(ret), use_container_width=True)


def seed_pouch():
    st.subheader('Your Seed Pouch', divider='blue')
    pouch_df = pd.read_csv(POUCH_PATH)

    st.write('Add seeds to your pouch:')
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        c = st.selectbox("Color", options=COLOR_LIST)
        add = st.button("Add")
    with col_2:
        s = st.selectbox("Seed", options=SEED_LIST)
    with col_3:
        n = st.number_input("Amount", value=None, placeholder="Enter a number...")
    if add:
        added = False
        for i in range(len(pouch_df)):
            if pouch_df.loc[i, 'Color'] == c and pouch_df.loc[i, 'Seed'] == s:
                pouch_df.loc[i, 'Number'] = n
                pouch_df.to_csv(POUCH_PATH, index=False)
                added = True
                break
        if not added:
            pouch_df.loc[-1] = [c, s, n]
            pouch_df.to_csv(POUCH_PATH, index=False)

    st.write('Your Seed Pouch:')
    st.dataframe(pouch_df, use_container_width=True)


moshling_see_combo_search()
num_mosh_every_combo()
seed_pouch()
