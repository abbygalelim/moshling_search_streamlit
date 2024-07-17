import pandas as pd
import streamlit as st
from tools.constants import GARDEN_PATH, MOSHLING_LIST
from tools.helper_functions import create_header, get_moshling_index, get_moshling_info

create_header('Edit Garden', 'Make changes to your garden! Add or remove moshlings.')

name_options = MOSHLING_LIST.copy()
name_options.insert(0, '')
name = st.selectbox('Choose a moshling:', options=name_options)

st.table(get_moshling_info([name], printable=True))

cols = st.columns(7)

with cols[0]:
    add = st.button("Add")
with cols[1]:
    remove = st.button("Remove")

if add or remove:
    df = pd.read_csv(GARDEN_PATH)
    i = get_moshling_index(name)
    df.loc[i, 'Owned'] = 'Yes' if add else 'No'
    df.to_csv(GARDEN_PATH, index=False)
