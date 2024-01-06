"""
# ???
???
"""

import os
import streamlit as st

st.session_state["env"] = os.environ.get("ENV", "dev")

st.sidebar.markdown("### What next?")
st.sidebar.markdown("Type in a query in natural language against your database.")

st.markdown("### Database connection")
conn = st.connection(st.session_state["env"], type="sql")
df = conn.query("select * from actor limit 10")

df
