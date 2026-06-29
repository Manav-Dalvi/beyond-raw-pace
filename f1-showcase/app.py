import streamlit as st
from components.f1_theme import inject_global_css, register_plotly_theme
from sections import hero, question, data, block1, block2, block3, block4, verdict, method, credits

st.set_page_config(
    page_title="Beyond Raw Pace - F1 Strategy",
    page_icon="🏁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

register_plotly_theme()
inject_global_css()

NAV_HTML = """
<nav class="f1-nav">
  <span class="brand">F1 STRATEGY</span>
  <a href="#question">The Question</a>
  <a href="#data">The Data</a>
  <a href="#block1">Circuit DNA</a>
  <a href="#block2">Safety Car</a>
  <a href="#block3">Penalty Timing</a>
  <a href="#block4">The Model</a>
  <a href="#verdict">Verdict</a>
  <a href="#method">Method</a>
</nav>
"""
st.markdown(NAV_HTML, unsafe_allow_html=True)

for render_fn in (
    hero.render,
    question.render,
    data.render,
    block1.render,
    block2.render,
    block3.render,
    block4.render,
    verdict.render,
    method.render,
    credits.render,
):
    render_fn()
    st.markdown('<div class="f1-divider"></div>', unsafe_allow_html=True)
