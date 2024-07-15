import streamlit as st
from tools.constants import COLOR_LIST, SEED_DICT, SEED_LIST
from tools.helper_functions import create_header, get_moshling_info
from tools.seed_search import search_moshling_by_seed

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
