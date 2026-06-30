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
    st.markdown(f'<span style="{_TTL}">Is winning about the machine, or the decisions?</span>', unsafe_allow_html=True)
    st.markdown(
        f'<span style="{_HOOK}">'
        f'Every race weekend, a team controls two very different things. One is the car: the product of a year of design, '
        f'a budget worth hundreds of millions, and an engine nobody can change on a Sunday. The other is the set of choices '
        f'made during the race itself, like when to pit, which tyres to fit, and how to react to a safety car.'
        f'</span>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div style="font-size:1rem;color:#9A9AA8;max-width:680px;line-height:1.6;margin-bottom:1.8rem;'
        f'font-family:\'Titillium Web\',sans-serif;">'
        f'The short version: the car is most of the story. Roughly 62 percent of what we can predict about whether a '
        f'driver scores points comes down to car quality alone. Strategy and the context around it add as much as about '
        f'one sixth more. That is small next to the car, but it is far from nothing. And unlike the car, it is something '
        f'a team can change from one race to the next.'
        f'</div>',
        unsafe_allow_html=True,
    )

    cols = st.columns(2)
    with cols[0]:
        countup(
            value=n["block4_supervised"]["car_quality_share"] * 100,
            label="Car quality",
            suffix="%", decimals=1, color="#E10600",
            caption="of predictable success traces to car quality",
            height=160,
        )
    with cols[1]:
        countup(
            value=n["block4_supervised"]["strategic_alpha"] * 100,
            label="Strategy and context",
            suffix="%", decimals=1, color="#00D2BE",
            caption="the broader influence of strategy and context, at most. A smaller, stricter measure of strategy alone is lower. Either way, it is the part a team can actually move.",
            height=160,
        )

    st.markdown(
        '<div class="card accent reveal" style="margin-top:1.5rem">'
        '<b style="color:#00D2BE">Strategy is a real, measurable edge.</b> Not the whole story, and not nothing. '
        'About one sixth of what is predictable about a result comes down to decisions, not the car.'
        '</div>',
        unsafe_allow_html=True,
    )
