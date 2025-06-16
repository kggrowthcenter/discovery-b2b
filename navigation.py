import streamlit as st
from time import sleep
import pandas as pd


def get_current_page_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("page", ["streamlit_app"])[0]

def make_sidebar():
    with st.sidebar:
        st.title("Sidebar Navigasi")
        if st.session_state.get("logged_in", False):
            st.page_link("pages/1_ASRI.py", label="Asri", icon="🎓")
            st.page_link("pages/2_LESTARI.py", label="Lestari", icon="🌎")

            st.write("")

            if st.button("Log out"):
                logout()
        elif get_current_page_name() != "streamlit_app":
            st.switch_page("streamlit_app.py")

def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("streamlit_app.py")
