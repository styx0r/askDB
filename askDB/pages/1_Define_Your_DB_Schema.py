import streamlit as st

from texts.db_schema import explanation
from functions.text import truncate


def set_db_schema_full_explanation(boolean: bool) -> None:
    st.session_state["db_schema_full_explanation"] = boolean


if "db_schema_full_explanation" not in st.session_state:
    set_db_schema_full_explanation(False)


st.sidebar.markdown("Definition of Database Schema for Generative AI")
st.markdown("# Explanation")

if st.session_state["db_schema_full_explanation"] == True:
    st.markdown(explanation)
    st.button("Show Less", on_click=set_db_schema_full_explanation, args=[False])
else:
    st.markdown(truncate(explanation, 280))
    st.button("Show More", on_click=set_db_schema_full_explanation, args=[True])

st.markdown("# Schema Definition")

# if there is no file just put in here no schema found and put a create button to create one with
# help of llm
