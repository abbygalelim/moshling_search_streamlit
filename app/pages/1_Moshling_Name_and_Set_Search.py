import streamlit as st
from tools.constants import MOSHLING_LIST, SET_AND_MOSHLINGS
from tools.helper_functions import create_header, get_moshling_info

create_header('Moshling Name Search', 'Search up moshlings by set and name')

set_list = list(SET_AND_MOSHLINGS.keys())
set_list.insert(0, '')
set_name = st.selectbox('Search by Set', options=set_list)

if set_name:
    mosh_set_results = SET_AND_MOSHLINGS[set_name]
    output = get_moshling_info(mosh_set_results, printable=True)
    st.table(output)

name = st.text_input('Search by Name')

mosh_results = []
for mosh in MOSHLING_LIST:
    if name.lower() in mosh.lower():
        mosh_results.append(mosh)

st.table(get_moshling_info(mosh_results, printable=True))
