import streamlit as st

from common.text import replace_db_placeholder
from common.page import set_session_state_var
from common.constants import SV_CREATE_SCHEMA
from common.db import execute_sql

from openai_integration.request import chat_completion
from config.prompts.create_db_schema import (
    sql_prompt,
    sql_prompt_system,
    create_db_schema_prompt,
    create_db_schema_system,
)

import logging


def display():
    st.title("Create Schema Definition")

    st.markdown("Waiting for appropriate SQL statements to get database information...")
    queries = chat_completion(sql_prompt, sql_prompt_system)["queries"]
    queries = replace_db_placeholder(queries)

    st.markdown("Executing SQL queries and collecting database information ...")
    queries_results = {}
    for query in queries:
        try:
            queries_results[query] = execute_sql(query)
        except Exception as e:
            logging.warning(
                f"The follwoing query raised the following exception:\n Query: {query}\n Exception: {e}"
            )

    st.markdown("Reading data base information ...")
    db_description = chat_completion(
        user_message=create_db_schema_prompt(queries_results),
        content_system=create_db_schema_system,
    )["db_description"]

    st.markdown("Suggestion based on your data:")
    # ToDo: show data and make it editable, add save button.
    # In case the file is already present,
    # directly go to the edit and save mode and
    # add an additional button to generate again with ai

    st.button("Back", on_click=set_session_state_var, args=[SV_CREATE_SCHEMA, False])
