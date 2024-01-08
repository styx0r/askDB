import streamlit as st

from common.page import set_session_state_var
from common.constants import SV_CREATE_SCHEMA


def display():
    st.title("Create Schema Definition")
    st.button("Back", on_click=set_session_state_var, args=[SV_CREATE_SCHEMA, False])
