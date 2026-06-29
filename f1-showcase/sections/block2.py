import streamlit as st
import streamlit.components.v1 as components
import os
from data_loader import numbers

_PLOTS = os.path.join(os.path.dirname(__file__), "..", "assets", "outputs", "plots")

_TAG  = "color:#E10600;text-transform:uppercase;letter-spacing:.25em;font-size:.75rem;font-weight:700;margin-bottom:.4rem;font-family:'Titillium Web',sans-serif;display:block;"
_TTL  = "font-size:clamp(1.8rem,4vw,3rem);font-weight:900;color:#E8E8E8;letter-spacing:-.02em;line-height:1.1;margin-bottom:.8rem;font-family:'Titillium Web',sans-serif;display:block;"
_HOOK = "font-size:1.1rem;color:#9A9AA8;max-width:680px;line-height:1.6;margin-bottom:1.8rem;font-family:'Titillium Web',sans-serif;display:block;"


def render():
    n = numbers()
    b2 = n["block2_iv"]

    st.markdown('<div id="block2" style="scroll-margin-top:80px;height:0;overflow:hidden;"></div>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TAG}">Block 2 — Causal Inference (IV)</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TTL}">The Safety-Car Gamble</span>', unsafe_allow_html=True)
    st.markdown(
        f'<span style="{_HOOK}">{n["translations"]["iv"]}'
        f' We used instrumental variables — safety-car deployment frequency per circuit '
        f'as an instrument — to isolate cause from correlation.</span>',
        unsafe_allow_html=True,
    )

    cols = st.columns(2)
    with cols[0]:
        st.markdown(
            f'<div class="card teal-accent reveal">'
            f'<div class="stat-num" style="color:#00D2BE">+{b2["q1_frontrunner_pp"]} pp</div>'
            f'<div class="stat-label">Front-runner (Q1 car quality)</div>'
            f'<div class="stat-caption">Pitting under safety car <b>helps</b> the fast car.</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
    with cols[1]:
        st.markdown(
            f'<div class="card accent reveal">'
            f'<div class="stat-num" style="color:#E10600">−{abs(b2["q5_backmarker_pp"])} pp</div>'
            f'<div class="stat-label">Backmarker (Q5 car quality)</div>'
            f'<div class="stat-caption">The same call <b>hurts</b> the slow car.</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    html_path = os.path.join(os.path.dirname(__file__), "..", "components", "two_drivers.html")
    with open(html_path, encoding="utf-8") as f:
        components.html(f.read(), height=320, scrolling=False)

    st.markdown(
        f'<div class="card reveal" style="margin-top:1rem">'
        f'<div style="color:#9A9AA8;font-size:.85rem;margin-bottom:.8rem;text-transform:uppercase;letter-spacing:.15em">Technical details</div>'
        f'<div style="display:flex;gap:2rem;flex-wrap:wrap;font-size:.9rem">'
        f'<div><b style="font-family:JetBrains Mono,monospace;color:#9A9AA8">{b2["ate_pp"]} pp</b>'
        f'<div style="color:#9A9AA8;font-size:.78rem">Aggregate 2SLS ATE</div></div>'
        f'<div><b style="font-family:JetBrains Mono,monospace;color:#9A9AA8">p = {b2["p"]}</b>'
        f'<div style="color:#9A9AA8;font-size:.78rem">Not significant</div></div>'
        f'<div><b style="font-family:JetBrains Mono,monospace;color:#9A9AA8">[{b2["ci_pp"][0]}, +{b2["ci_pp"][1]}] pp</b>'
        f'<div style="color:#9A9AA8;font-size:.78rem">95% CI</div></div>'
        f'<div><b style="font-family:JetBrains Mono,monospace;color:#E8E8E8">{b2["partial_F"]}</b>'
        f'<div style="color:#9A9AA8;font-size:.78rem">Partial F (instrument relevance)</div></div>'
        f'<div><b style="font-family:JetBrains Mono,monospace;color:#E8E8E8">{b2["sc_races"]}</b>'
        f'<div style="color:#9A9AA8;font-size:.78rem">Safety-car races</div></div>'
        f'</div></div>',
        unsafe_allow_html=True,
    )

    col_a, col_b = st.columns(2)
    with col_a:
        p = os.path.join(_PLOTS, "b2_01_dag.png")
        if os.path.exists(p):
            st.image(p, caption="Causal DAG — specifying confounders before estimation. SC deployment frequency is the instrument for pit decisions.", use_container_width=True)
    with col_b:
        p = os.path.join(_PLOTS, "b2_04_hte_forest.png")
        if os.path.exists(p):
            st.image(p, caption="Heterogeneous treatment effects by car-quality quintile. Front-runners benefit; backmarkers are hurt. This heterogeneity is the main finding.", use_container_width=True)
