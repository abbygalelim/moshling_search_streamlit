import streamlit as st
from tools.constants import GARDEN_PATH, REPO_PATH
from tools.helper_functions import create_header

create_header('Help')

readme_url = 'https://github.com/abbygalelim/moshling_search_streamlit'
st.markdown(
    'Information can be found in the `moshling_search_streamlit` GitHub repo [README.md](%s).' % readme_url,
    unsafe_allow_html=True,
)
st.write('')
st.write('Where is my `moshling_search_streamlit` folder located?')
st.markdown(f'- `{REPO_PATH}`')
st.write('Where is my `garden.csv` file located?')
st.markdown(f'- `{GARDEN_PATH}`')

st.markdown(
    '''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    ''',
    unsafe_allow_html=True,
)
