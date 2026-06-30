import streamlit as st
from components.countup import countup
from data_loader import numbers

_TAG  = "color:#E10600;text-transform:uppercase;letter-spacing:.25em;font-size:.75rem;font-weight:700;margin-bottom:.4rem;font-family:'Titillium Web',sans-serif;display:block;"
_TTL  = "font-size:clamp(1.8rem,4vw,3rem);font-weight:900;color:#E8E8E8;letter-spacing:-.02em;line-height:1.1;margin-bottom:.8rem;font-family:'Titillium Web',sans-serif;display:block;"
_HOOK = "font-size:1.1rem;color:#9A9AA8;max-width:680px;line-height:1.6;margin-bottom:1.8rem;font-family:'Titillium Web',sans-serif;display:block;"


def render():
    n = numbers()
    s = n["scale"]

    st.markdown('<div id="data" style="scroll-margin-top:80px;height:0;overflow:hidden;"></div>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TAG}">The Data</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TTL}">22 Seasons. One Question.</span>', unsafe_allow_html=True)
    st.markdown(
        f'<span style="{_HOOK}">Before asking what strategy does, we needed enough data '
        f'to actually measure it. Here is what we built the analysis on.</span>',
        unsafe_allow_html=True,
    )

    cols = st.columns(4)
    with cols[0]:
        countup(value=s["driver_races"], label="Driver-races", color="#E8E8E8", height=130)
    with cols[1]:
        countup(value=s["seasons"], label="Seasons", color="#E8E8E8", height=130)
    with cols[2]:
        countup(value=s["variables"], label="Variables", color="#E8E8E8", height=130)
    with cols[3]:
        countup(value=len(s["sources"]), label="Data sources", color="#E8E8E8", height=130)

    st.markdown(
        f'<div class="card reveal" style="margin-top:1rem">'
        f'<div style="color:#9A9AA8;font-size:.85rem;margin-bottom:.6rem;text-transform:uppercase;letter-spacing:.15em">Coverage</div>'
        f'<div style="color:#E8E8E8">'
        f'Seasons <b style="color:#00D2BE">{s["season_start"]}-{s["season_end"]}</b> · '
        f'{s["circuits_clustered"]} circuits clustered · '
        f'{s["sessions_missing"]} FastF1 sessions missing (noted, not imputed) · '
        f'Drivers score points in ~{int(s["scored_point_base_rate"]*100)}% of races'
        f'</div>'
        f'<div style="margin-top:.8rem;color:#9A9AA8;font-size:.85rem">'
        f'Sources: {" · ".join(s["sources"])}'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
