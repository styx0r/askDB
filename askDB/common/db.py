import streamlit as st


def execute_sql(query: str):
    conn = st.connection(st.session_state["env"], type="sql")
    return conn.query(query, ttl=0)
