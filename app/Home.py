import streamlit as st


def main():
    st.header("Welcome to :blue[BlueShift's] Moshling CLI Tool!", divider='rainbow')
    text = '''
    This app gives avid Moshling collecters on Moshi Online the best chance of
    catching moshlings while minimizing their efforts.
    '''
    st.markdown(f'<p style="font-size: 20px"> {text} </p>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
