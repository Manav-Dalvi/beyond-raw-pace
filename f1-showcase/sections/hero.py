import streamlit as st
import streamlit.components.v1 as components
import os


def render():
    st.markdown('<section id="hero"></section>', unsafe_allow_html=True)
    html_path = os.path.join(os.path.dirname(__file__), "..", "components", "hero.html")
    with open(html_path, encoding="utf-8") as f:
        components.html(f.read(), height=560, scrolling=False)
