import streamlit as st

_TAG = "color:#E10600;text-transform:uppercase;letter-spacing:.25em;font-size:.75rem;font-weight:700;margin-bottom:.4rem;font-family:'Titillium Web',sans-serif;display:block;"
_TTL = "font-size:clamp(1.8rem,4vw,3rem);font-weight:900;color:#E8E8E8;letter-spacing:-.02em;line-height:1.1;margin-bottom:.8rem;font-family:'Titillium Web',sans-serif;display:block;"


def render():
    st.markdown('<div id="credits" style="scroll-margin-top:80px;height:0;overflow:hidden;"></div>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TAG}">Team &amp; Credits</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TTL}">About This Project</span>', unsafe_allow_html=True)

    cols = st.columns(2)
    with cols[0]:
        st.markdown(
            '<div class="card reveal">'
            '<div style="color:#9A9AA8;font-size:.78rem;text-transform:uppercase;letter-spacing:.18em;margin-bottom:.8rem">The Team</div>'
            '<div style="color:#E8E8E8;font-size:1rem;line-height:2">Manav Madhukar Dalvi  ·  Bademba Drammeh  ·  Sasha Marie Stühmer'
            '<br><span style="color:#9A9AA8;font-size:.9rem">TU Dortmund · Data and AI in Economics</span>'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="card reveal" style="margin-top:.8rem">'
            '<div style="color:#9A9AA8;font-size:.78rem;text-transform:uppercase;letter-spacing:.18em;margin-bottom:.8rem">Data Sources</div>'
            '<div style="color:#E8E8E8;font-size:.9rem;line-height:1.8">'
            'Jolpica / Ergast API (race results, 2003–2024)<br>'
            'FastF1 (telemetry &amp; session data)<br>'
            'Open-Meteo (weather data)'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )
    with cols[1]:
        st.markdown(
            '<div class="card reveal">'
            '<div style="color:#9A9AA8;font-size:.78rem;text-transform:uppercase;letter-spacing:.18em;margin-bottom:.8rem">Built with</div>'
            '<div style="color:#E8E8E8;font-size:.9rem;line-height:1.8">'
            'Streamlit · Plotly · pandas<br>'
            'Titillium Web · JetBrains Mono (Google Fonts)<br>'
            'Canvas API · IntersectionObserver'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="card accent reveal" style="margin-top:.8rem">'
            '<div style="color:#9A9AA8;font-size:.78rem;text-transform:uppercase;letter-spacing:.18em;margin-bottom:.8rem">LLM-Assistance Disclosure</div>'
            '<div style="color:#9A9AA8;font-size:.88rem;line-height:1.5">'
            'Large language models (Claude, ChatGPT, Gemini) were used as coding assistants '
            'during the development of this project. All analytical decisions, '
            'interpretations, and the academic content were made and verified by the team. '
            "This use is consistent with the course's academic integrity guidelines."
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div style="text-align:center;color:#9A9AA8;font-size:.8rem;margin-top:3rem;padding-bottom:2rem;'
        "font-family:'Titillium Web',sans-serif;\">"
        'No trademarked F1, team, or driver assets are used on this site. '
        'Design is original, F1-inspired work.'
        '</div>',
        unsafe_allow_html=True,
    )
