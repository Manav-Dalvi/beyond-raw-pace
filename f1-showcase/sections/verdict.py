import streamlit as st
from data_loader import numbers

_TAG = "color:#E10600;text-transform:uppercase;letter-spacing:.25em;font-size:.75rem;font-weight:700;margin-bottom:.4rem;font-family:'Titillium Web',sans-serif;display:block;"
_TTL = "font-size:clamp(1.8rem,4vw,3rem);font-weight:900;color:#E8E8E8;letter-spacing:-.02em;line-height:1.1;margin-bottom:.8rem;font-family:'Titillium Web',sans-serif;display:block;"


def render():
    n = numbers()
    b2 = n["block2_iv"]
    b3 = n["block3_backdoor"]

    st.markdown('<div id="verdict" style="scroll-margin-top:80px;height:0;overflow:hidden;"></div>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TAG}">The Verdict</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TTL}">Strategy is the Edge in the Car\'s Shadow</span>', unsafe_allow_html=True)

    cells = "".join([
        f'<div style="width:16px;height:16px;background:{"#E8E8E8" if (i+j)%2==0 else "#2A2A38"}"></div>'
        for j in range(2) for i in range(20)
    ])
    st.markdown(
        f'<div style="display:flex;flex-wrap:wrap;gap:0;margin-bottom:1.5rem;opacity:.4">{cells}</div>',
        unsafe_allow_html=True,
    )

    takeaways = [
        {
            "tag": "Finding 1", "color": "#E10600",
            "title": "Same call. Opposite outcomes.",
            "body": f"Pitting under a safety car yields <b style='color:#00D2BE'>+{b2['q1_frontrunner_pp']} pp</b> "
                    f"for a front-runner and <b style='color:#E10600'>−{abs(b2['q5_backmarker_pp'])} pp</b> "
                    f"for a backmarker. The aggregate effect is negative and not statistically significant "
                    f"(p = {b2['p']}). The story is the heterogeneity.",
        },
        {
            "tag": "Finding 2", "color": "#FFF200",
            "title": "Tracks have personalities.",
            "body": "Three circuit archetypes — Strategy-dependent, All-rounders, Chaos-friendly — "
                    "each creating different opportunity spaces for strategy to matter. "
                    "The clustering is stable (ARI = 1.000 across two algorithms).",
        },
        {
            "tag": "Finding 3", "color": "#00D2BE",
            "title": "A +12.8 pp advantage. Mostly unclaimed.",
            "body": f"Timing grid penalties at low-cost circuits is worth <b style='color:#00D2BE'>+{b3['ate_pp']} pp</b>. "
                    f"Evidence is marginally significant (p ≈ {b3['p']}), passes refutation. "
                    f"Teams don't appear to exploit it — yet.",
        },
    ]

    cols = st.columns(3)
    for col, t in zip(cols, takeaways):
        with col:
            st.markdown(
                f'<div class="card reveal" style="border-top:3px solid {t["color"]};height:100%">'
                f'<div style="color:{t["color"]};font-size:.72rem;text-transform:uppercase;letter-spacing:.2em;margin-bottom:.5rem">{t["tag"]}</div>'
                f'<div style="font-size:1rem;font-weight:700;color:#E8E8E8;margin-bottom:.6rem">{t["title"]}</div>'
                f'<div style="font-size:.88rem;color:#9A9AA8;line-height:1.5">{t["body"]}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

    st.markdown(
        f'<div class="card accent reveal" style="margin-top:1.5rem;text-align:center;padding:2rem">'
        f'<div style="font-size:1.4rem;font-weight:900;color:#E8E8E8;letter-spacing:-.01em;margin-bottom:.6rem;font-family:\'Titillium Web\',sans-serif;">'
        f'Strategy is a real, measurable edge — worth about one-sixth of what\'s predictable.'
        f'</div>'
        f'<div style="color:#9A9AA8;font-size:1rem;max-width:580px;margin:auto;font-family:\'Titillium Web\',sans-serif;">'
        f'At least one slice of it is currently unclaimed. '
        f'The gap between what the data says is possible and what teams actually do is the project\'s headline.'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
