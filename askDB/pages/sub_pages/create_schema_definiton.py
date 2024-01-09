import streamlit as st

from common.page import set_session_state_var
from common.constants import SV_CREATE_SCHEMA

from openai_integration.request import chat_completion
from config.prompts.create_db_schema import sql_prompt


def display():
    st.title("Create Schema Definition")

    st.markdown("Waiting for appropriate SQL statements to get database information...")
    queries = chat_completion(sql_prompt)["queries"]

    st.markdown("Executing SQL queries and collecting database information ...")
    for query in queries:
        

    st.markdown("Reading data base information ...")
    sql_statements = chat_completion(user_message=sql_prompt)
    sql_statements

    st.markdown("Suggestion based on your data:")

    st.button("Back", on_click=set_session_state_var, args=[SV_CREATE_SCHEMA, False])
