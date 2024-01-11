import streamlit as st

from common.text import replace_db_placeholder
from common.page import set_session_state_var
from common.constants import SV_CREATE_SCHEMA
from common.db import execute_sql

from openai_integration.request import chat_completion
from config.prompts.create_db_schema import sql_prompt


def display():
    st.title("Create Schema Definition")

    st.markdown("Waiting for appropriate SQL statements to get database information...")
    queries = chat_completion(sql_prompt)["queries"]
    queries = replace_db_placeholder(queries)

    st.markdown("Executing SQL queries and collecting database information ...")
    # ToDo: change this to dict with query as key and result as value
    queries_results = []
    for query in queries:
        # ToDo: Error handling in case the query is not executable on the database
        queries_results.append(execute_sql(query))

    st.markdown("Reading data base information ...")
    sql_statements = chat_completion(user_message=sql_prompt)
    sql_statements

    st.markdown("Suggestion based on your data:")

    st.button("Back", on_click=set_session_state_var, args=[SV_CREATE_SCHEMA, False])
