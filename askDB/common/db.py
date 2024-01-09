import streamlit as st


def execute_sql(query):
    conn = st.connection(st.session_state.env)
    return conn.query(query)
