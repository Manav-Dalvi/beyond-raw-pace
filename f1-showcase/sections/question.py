import streamlit as st
from components.countup import countup
from data_loader import numbers

_TAG  = "color:#E10600;text-transform:uppercase;letter-spacing:.25em;font-size:.75rem;font-weight:700;margin-bottom:.4rem;font-family:'Titillium Web',sans-serif;display:block;"
_TTL  = "font-size:clamp(1.8rem,4vw,3rem);font-weight:900;color:#E8E8E8;letter-spacing:-.02em;line-height:1.1;margin-bottom:.8rem;font-family:'Titillium Web',sans-serif;display:block;"
_HOOK = "font-size:1.1rem;color:#9A9AA8;max-width:680px;line-height:1.6;margin-bottom:1.8rem;font-family:'Titillium Web',sans-serif;display:block;"


def render():
    n = numbers()
    st.markdown('<div id="question" style="scroll-margin-top:80px;height:0;overflow:hidden;"></div>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TAG}">The Question</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TTL}">The Machine vs. The Mind</span>', unsafe_allow_html=True)
    st.markdown(
        f'<span style="{_HOOK}">Is winning about the car or the decisions? '
        f'We measured exactly how much each contributes — across 22 seasons of Formula 1.</span>',
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    with cols[0]:
        countup(
            value=n["block4_supervised"]["car_quality_share"] * 100,
            label="Car quality",
            suffix="%", decimals=1, color="#E10600",
            caption="Construction, engine, chassis — the machine.",
            height=160,
        )
    with cols[1]:
        countup(
            value=n["block4_supervised"]["strategic_alpha"] * 100,
            label="Strategy",
            suffix="%", decimals=1, color="#00D2BE",
            caption=n["translations"]["alpha"],
            height=160,
        )
    with cols[2]:
        countup(
            value=(1 - n["block4_supervised"]["car_quality_share"] - n["block4_supervised"]["strategic_alpha"]) * 100,
            label="Other factors",
            suffix="%", decimals=1, color="#9A9AA8",
            caption="Weather, incidents, driver variation, noise.",
            height=160,
        )

    st.markdown(
        '<div class="card accent reveal" style="margin-top:1.5rem">'
        '<b style="color:#00D2BE">Strategy is a real, measurable edge</b> — not the whole story, not nothing. '
        'About one-sixth of what is predictable about a result comes down to decisions, not the car.'
        '</div>',
        unsafe_allow_html=True,
    )
