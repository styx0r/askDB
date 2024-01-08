"""
# ???
???
"""

import streamlit as st
from common.page import init_session_state

init_session_state()

st.sidebar.markdown("### What next?")
st.sidebar.markdown("Type in a query in natural language against your database.")

st.markdown("### Database connection")
conn = st.connection(st.session_state["env"], type="sql")
df = conn.query("select * from actor limit 10")

df
