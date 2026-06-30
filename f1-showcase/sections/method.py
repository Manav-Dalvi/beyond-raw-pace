import streamlit as st

_TAG  = "color:#E10600;text-transform:uppercase;letter-spacing:.25em;font-size:.75rem;font-weight:700;margin-bottom:.4rem;font-family:'Titillium Web',sans-serif;display:block;"
_TTL  = "font-size:clamp(1.8rem,4vw,3rem);font-weight:900;color:#E8E8E8;letter-spacing:-.02em;line-height:1.1;margin-bottom:.8rem;font-family:'Titillium Web',sans-serif;display:block;"
_HOOK = "font-size:1.1rem;color:#9A9AA8;max-width:680px;line-height:1.6;margin-bottom:1.8rem;font-family:'Titillium Web',sans-serif;display:block;"


def render():
    st.markdown('<div id="method" style="scroll-margin-top:80px;height:0;overflow:hidden;"></div>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TAG}">Behind the Method</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TTL}">How We Kept It Honest</span>', unsafe_allow_html=True)
    st.markdown(
        f'<span style="{_HOOK}">For the technical panel. '
        f'The non-technical reader can skip this. The story above stands on its own.</span>',
        unsafe_allow_html=True,
    )

    methods = [
        ("Walk-forward validation",
         "Never random CV. Models are trained on all prior seasons and tested on the next. "
         "This mirrors how a real forecast works: we only ever showed the model the past."),
        ("Instrumental variables (Block 2)",
         "We use each circuit's historical safety-car frequency as an instrument for pit decisions. "
         "Instrument relevance confirmed: partial F = 74.37. "
         "Aggregate 2SLS ATE = -10.1 pp (p = 0.294, not significant). "
         "Finding is the heterogeneity across car-quality quintiles."),
        ("Backdoor causal estimate (Block 3)",
         "DoWhy with a backdoor adjustment for confounders. "
         "ATE = +12.8 pp, p about 0.063 (marginal). "
         "Both refutation tests (random common cause, placebo treatment) pass. "
         "Strategic-timing tests return null. Teams do not appear to exploit the pattern."),
        ("Pre-specified thresholds",
         "The penalty-cost elasticity threshold (β = 0.5863) was fixed before analysis. "
         "It was not recomputed post-hoc to sharpen the finding."),
        ("Directed Acyclic Graphs (DAGs)",
         "Causal structure was specified via DAGs before estimation. "
         "Confounders (team budget, circuit characteristics) were explicitly modelled."),
        ("Honestly reported null results",
         "Block 2 aggregate is negative and not significant, stated plainly. "
         "Block 3 is marginal. We say 'evidence of,' not 'proof.' "
         "We did not cherry-pick significant sub-groups after finding a null aggregate."),
    ]

    for title, body in methods:
        st.markdown(
            f'<div class="card reveal" style="margin-bottom:.7rem">'
            f'<div style="font-weight:700;color:#E8E8E8;margin-bottom:.3rem">{title}</div>'
            f'<div style="color:#9A9AA8;font-size:.9rem;line-height:1.5">{body}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
