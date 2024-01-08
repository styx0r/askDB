import os
import streamlit as st


def init_session_state():
    st.session_state["env"] = os.environ.get("ENV", "dev")
    if "OPENAI_API_KEY" not in os.environ:
        st.markdown(
            "Please set the OPENAI_API_KEY environment variable in order to successfully start the app."
        )


def set_session_state_var(var_name: str, value: any) -> None:
    st.session_state[var_name] = value


def init_session_state_var(var_name: str, value: any) -> None:
    if var_name not in st.session_state:
        set_session_state_var(var_name, value)
