"""
# ???
???
"""

import streamlit as st
from common.page import init_session_state
from common.db import execute_sql

init_session_state()

st.sidebar.markdown("### What next?")
st.sidebar.markdown("Type in a query in natural language against your database.")

st.markdown("### Database connection")
df = execute_sql("select * from actor limit 10")

st.dataframe(df)
