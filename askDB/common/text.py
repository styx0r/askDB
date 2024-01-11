import streamlit as st
from typing import List

from common.constants import DB_PLACEHOLDER


def truncate(text: str, length=300) -> str:
    return text if len(text) < length else text[:length]


def replace_db_placeholder(queries: List[str]):
    [
        q.replace(
            DB_PLACEHOLDER,
            st.secrets["connections"][st.session_state["env"]]["database"],
        )
        for q in queries
    ]
