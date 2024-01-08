import os
import streamlit as st

from texts.db_schema import explanation
from common.text import truncate

from common.page import (
    init_session_state,
    set_session_state_var,
    init_session_state_var,
)
from common.constants import SV_CREATE_SCHEMA, SV_DB_SCHEMA_FULL_EXPLANATION

from pages.sub_pages.create_schema_definiton import display as create_schema_page

init_session_state()

SCHEMA_DEFINITION_FILE = (
    f"config/schema_definitions/{st.session_state.env}.schema_defintion"
)

init_session_state_var(SV_DB_SCHEMA_FULL_EXPLANATION, False)
init_session_state_var(SV_CREATE_SCHEMA, False)

if st.session_state[SV_CREATE_SCHEMA]:
    create_schema_page()
else:
    st.sidebar.markdown("Definition of Database Schema for Generative AI")
    st.markdown("# Explanation")

    if st.session_state[SV_DB_SCHEMA_FULL_EXPLANATION] == True:
        st.markdown(explanation)
        st.button(
            "Show Less",
            on_click=set_session_state_var,
            args=[SV_DB_SCHEMA_FULL_EXPLANATION, False],
        )
    else:
        st.markdown(truncate(explanation, 280))
        st.button(
            "Show More",
            on_click=set_session_state_var,
            args=[SV_DB_SCHEMA_FULL_EXPLANATION, True],
        )

    st.markdown("# Schema Definition")

    if not os.path.isfile(SCHEMA_DEFINITION_FILE):
        st.button(
            "Create Schema Definition",
            on_click=set_session_state_var,
            args=[SV_CREATE_SCHEMA, True],
        )
    # if there is no file just put in here no schema found and put a create button to create one with
    # help of llm
