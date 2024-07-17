import streamlit as st
from tools.constants import MOSHLING_RARITY
from tools.helper_functions import create_header, get_moshling_info

create_header('Rarity Search', 'Search moshlings by rarity.')

rarity_choices = {'': -1, 'Common': 3, 'Uncommon': 2, 'Rare': 1, 'Ultra Rare': 0, 'Mission': -1}
rarity = st.selectbox('Choose a rarity', options=list(rarity_choices.keys()))
owned = st.selectbox('Filter by owned', options=list(['', 'Owned', 'Not Owned']))

if rarity:
    rarity_id = rarity_choices[rarity]
    df = get_moshling_info(MOSHLING_RARITY[rarity_id], printable=True)
    owned_mosh = []
    not_owned_mosh = []

    total, owned_count, not_owned_count = len(df), 0, 0
    for i in range(total):
        if df.loc[i, 'Owned'] == 'Yes':
            owned_count += 1
            owned_mosh.append(df.loc[i, 'Name'])
        else:
            not_owned_count += 1
            not_owned_mosh.append(df.loc[i, 'Name'])

    col_1, col_2 = st.columns(2)
    with col_1:
        st.write(f'Owned: {owned_count}/{total}')
    with col_2:
        st.write(f'Not Owned: {not_owned_count}/{total}')

    if owned == 'Owned':
        st.dataframe(get_moshling_info(owned_mosh, printable=True))
    elif owned == 'Not Owned':
        st.dataframe(get_moshling_info(not_owned_mosh, printable=True))
    else:
        st.dataframe(df)
