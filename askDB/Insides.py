"""
# ???
???
"""

import os
import streamlit as st

st.session_state["env"] = os.environ.get("ENV", "dev")
if "OPENAI_API_KEY" not in os.environ:
    st.markdown(
        "Please set the OPENAI_API_KEY environment variable in order to successfully start the app."
    )

st.sidebar.markdown("### What next?")
st.sidebar.markdown("Type in a query in natural language against your database.")

st.markdown("### Database connection")
conn = st.connection(st.session_state["env"], type="sql")
df = conn.query("select * from actor limit 10")

df
