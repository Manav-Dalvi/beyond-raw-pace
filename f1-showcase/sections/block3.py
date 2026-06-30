import streamlit as st
import streamlit.components.v1 as components
import os
from data_loader import numbers

_PLOTS = os.path.join(os.path.dirname(__file__), "..", "assets", "outputs", "plots")

_TAG  = "color:#E10600;text-transform:uppercase;letter-spacing:.25em;font-size:.75rem;font-weight:700;margin-bottom:.4rem;font-family:'Titillium Web',sans-serif;display:block;"
_TTL  = "font-size:clamp(1.8rem,4vw,3rem);font-weight:900;color:#E8E8E8;letter-spacing:-.02em;line-height:1.1;margin-bottom:.8rem;font-family:'Titillium Web',sans-serif;display:block;"
_HOOK = "font-size:1.1rem;color:#9A9AA8;max-width:680px;line-height:1.6;margin-bottom:1.8rem;font-family:'Titillium Web',sans-serif;display:block;"

METER_HTML = """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700&family=Titillium+Web:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box;}
  body{background:transparent;font-family:'Titillium Web',sans-serif;padding:1rem;}
  .layout{display:flex;gap:2rem;align-items:flex-start;flex-wrap:wrap;}
  .meter-wrap{display:flex;flex-direction:column;align-items:center;gap:.6rem;flex-shrink:0;}
  .meter-label{font-size:.78rem;text-transform:uppercase;letter-spacing:.18em;color:#9A9AA8;}
  .meter-track{width:72px;height:200px;background:#1F1F2B;border:1px solid #2A2A38;border-radius:8px;position:relative;overflow:hidden;}
  .meter-fill{position:absolute;bottom:0;width:100%;height:0%;background:linear-gradient(to top,#00D2BE,#00D2BE88);transition:height 1.2s cubic-bezier(.2,.8,.2,1);}
  .meter-unclaimed{position:absolute;bottom:0;width:100%;height:0%;background:repeating-linear-gradient(45deg,#2A2A38,#2A2A38 4px,#1F1F2B 4px,#1F1F2B 8px);transition:height 1.2s 1s cubic-bezier(.2,.8,.2,1);}
  .meter-val{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:1.3rem;color:#00D2BE;}
  .info{flex:1;min-width:220px;}
  .info-title{font-size:1rem;font-weight:700;color:#E8E8E8;margin-bottom:.6rem;}
  .info-item{display:flex;gap:.6rem;align-items:flex-start;margin-bottom:.5rem;}
  .dot{width:9px;height:9px;border-radius:50%;flex-shrink:0;margin-top:.3rem;}
  .info-text{font-size:.85rem;color:#9A9AA8;line-height:1.4;}
  .caveat{margin-top:.8rem;padding:.7rem 1rem;background:#1F1F2B;border:1px solid #2A2A38;border-left:3px solid #FFF200;border-radius:8px;font-size:.8rem;color:#9A9AA8;line-height:1.5;}
</style>
</head>
<body>
<div class="layout">
  <div class="meter-wrap">
    <div class="meter-label">Available</div>
    <div class="meter-track">
      <div class="meter-fill" id="fillBar"></div>
      <div class="meter-unclaimed" id="unclaimedBar"></div>
    </div>
    <div class="meter-val">+12.8 pp</div>
    <div style="font-size:.7rem;color:#9A9AA8;text-align:center">Penalty timing<br>advantage</div>
  </div>
  <div class="info">
    <div class="info-title">Points left on the table</div>
    <div class="info-item">
      <div class="dot" style="background:#00D2BE"></div>
      <div class="info-text"><b style="color:#00D2BE">+12.8 pp advantage</b> exists for timing unavoidable grid penalties at low-cost circuits. The DoWhy backdoor estimate survives both refutation tests.</div>
    </div>
    <div class="info-item">
      <div class="dot" style="background:#2A2A38"></div>
      <div class="info-text"><b style="color:#9A9AA8">Teams don't appear to take it.</b> Strategic-timing tests return null: no evidence teams exploit this pattern.</div>
    </div>
    <div class="caveat">
      <b style="color:#FFF200">Statistical caveat:</b> p about 0.063, marginally significant. Frame as "evidence of," not "proof." Both DoWhy refutation tests pass.
    </div>
  </div>
</div>
<script>
  var obs = new IntersectionObserver(function(entries) {
    if (!entries[0].isIntersecting) return;
    obs.disconnect();
    setTimeout(function() {
      document.getElementById('fillBar').style.height = '100%';
      setTimeout(function() { document.getElementById('unclaimedBar').style.height = '88%'; }, 900);
    }, 300);
  }, {threshold:0.3});
  obs.observe(document.body);
</script>
</body>
</html>"""


def render():
    n = numbers()
    b3 = n["block3_backdoor"]

    st.markdown('<div id="block3" style="scroll-margin-top:80px;height:0;overflow:hidden;"></div>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TAG}">Block 3: Causal Inference (Backdoor)</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TTL}">A smart move that teams mostly do not make</span>', unsafe_allow_html=True)
    st.markdown(
        f'<span style="{_HOOK}">{n["translations"]["penalty"]}'
        f' A backdoor causal estimate (with DoWhy refutation checks) reveals a '
        f'real but mostly unclaimed strategic edge.</span>',
        unsafe_allow_html=True,
    )

    cols = st.columns([1, 2])
    with cols[0]:
        st.markdown(
            f'<div class="card teal-accent reveal">'
            f'<div class="stat-num" style="color:#00D2BE">+{b3["ate_pp"]} pp</div>'
            f'<div class="stat-label">Penalty timing advantage</div>'
            f'<div class="stat-caption">Timing an unavoidable grid penalty at a low-cost circuit.</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="card reveal" style="margin-top:.8rem">'
            f'<div class="stat-num" style="color:#FFF200;font-size:1.8rem">p ≈ {b3["p"]}</div>'
            f'<div class="stat-label">Marginal significance</div>'
            f'<div class="stat-caption">Both DoWhy refutation tests pass.</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
    with cols[1]:
        components.html(METER_HTML, height=320, scrolling=False)

    p = os.path.join(_PLOTS, "b3_01_elasticity_table.png")
    if os.path.exists(p):
        st.image(p, caption="Penalty-cost elasticity by circuit. Circuits below the median threshold (β < 0.5863) are identified as low-cost venues where timing a penalty preserves the most position.", use_container_width=True)
