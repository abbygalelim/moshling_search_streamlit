import streamlit as st
from tools.constants import GARDEN_DATA, SET_AND_MOSHLINGS
from tools.helper_functions import create_header, get_moshling_index, get_moshling_info


def get_set_stats():
    full_sets, almost_full_sets, empty_sets = [], [], []

    for set, mosh_list in SET_AND_MOSHLINGS.items():
        total_count = len(mosh_list)
        owned_count = 0

        for mosh in mosh_list:
            mosh_i = get_moshling_index(mosh)
            if GARDEN_DATA.loc[mosh_i, 'Owned'] == 'Yes':
                owned_count += 1

        if total_count == owned_count:
            full_sets.append(set)
        elif total_count - owned_count == 1:
            almost_full_sets.append(set)
        elif owned_count == 0:
            empty_sets.append(set)

    st.write(f'You have completed {len(full_sets)} sets')
    st.table(full_sets)
    st.write(f'You are 1 moshling away from completing {len(almost_full_sets)} sets')
    st.table(almost_full_sets)
    st.write(f'You have not captured any moshlings in {len(empty_sets)} sets')
    st.table(empty_sets)


# streamlit run app/Home.py
def main():
    create_header(
        "Welcome to :blue[BlueShift's] Moshling Garden",
        '''
        Use this app to search and sort through the moshlings in Moshi Online
        by seed combinations, name, set, ownership, and rarity.
        ''',
    )

    st.subheader('Moshlings in your garden', divider='blue')

    mosh_results = []
    for i in range(len(GARDEN_DATA)):
        if GARDEN_DATA.loc[i, 'Owned'] == 'Yes':
            mosh_results.append(GARDEN_DATA.loc[i, 'Name'])

    st.write(f'You own {len(mosh_results)}/{len(GARDEN_DATA)} moshlings')
    st.dataframe(get_moshling_info(mosh_results, printable=True))

    st.subheader('Stats', divider='blue')
    get_set_stats()


if __name__ == "__main__":
    main()
