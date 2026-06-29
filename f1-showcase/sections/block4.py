import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import json, os
from data_loader import numbers

_PLOTS = os.path.join(os.path.dirname(__file__), "..", "assets", "outputs", "plots")

_TAG  = "color:#E10600;text-transform:uppercase;letter-spacing:.25em;font-size:.75rem;font-weight:700;margin-bottom:.4rem;font-family:'Titillium Web',sans-serif;display:block;"
_TTL  = "font-size:clamp(1.8rem,4vw,3rem);font-weight:900;color:#E8E8E8;letter-spacing:-.02em;line-height:1.1;margin-bottom:.8rem;font-family:'Titillium Web',sans-serif;display:block;"
_HOOK = "font-size:1.1rem;color:#9A9AA8;max-width:680px;line-height:1.6;margin-bottom:1.8rem;font-family:'Titillium Web',sans-serif;display:block;"

LADDER_HTML = """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700&family=Titillium+Web:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box;}
  body{background:transparent;font-family:'Titillium Web',sans-serif;padding:1rem;}
  .rung{display:flex;align-items:center;gap:.8rem;margin-bottom:.8rem;opacity:0;transform:translateX(-12px);transition:opacity .4s ease,transform .4s ease;}
  .rung.show{opacity:1;transform:translateX(0);}
  .model-tag{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:.85rem;color:#9A9AA8;width:32px;flex-shrink:0;}
  .bar-outer{flex:1;height:30px;background:#1F1F2B;border-radius:6px;overflow:hidden;border:1px solid #2A2A38;}
  .bar-inner{height:100%;width:0%;border-radius:6px;transition:width .8s cubic-bezier(.2,.8,.2,1);display:flex;align-items:center;padding-left:.5rem;font-family:'JetBrains Mono',monospace;font-size:.78rem;font-weight:700;color:#15151E;white-space:nowrap;}
  .auc-val{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:.88rem;min-width:52px;text-align:right;flex-shrink:0;}
</style>
</head>
<body>
<div id="ladder"></div>
<script>
var data = LADDER_DATA_PLACEHOLDER;
var BAR_COLORS = ['#3A3A50','#5A4ABF','#8B49A6','#C80500','#E10600'];
var minAUC = 0.80, maxAUC = 0.88;
var ladder = document.getElementById('ladder');
data.forEach(function(d,i) {
  var pct = ((d.auc - minAUC)/(maxAUC - minAUC)*100).toFixed(1);
  var el = document.createElement('div');
  el.className = 'rung';
  var isFinal = i === data.length-1;
  el.innerHTML = '<div class="model-tag">'+d.id+'</div>'
    +'<div class="bar-outer"><div class="bar-inner" id="bar'+i+'" style="background:'+BAR_COLORS[i]+'">'+d.label+'</div></div>'
    +'<div class="auc-val" style="color:'+(isFinal?'#00D2BE':'#9A9AA8')+'">'+d.auc.toFixed(4)+'</div>';
  ladder.appendChild(el);
});
var obs = new IntersectionObserver(function(entries) {
  if (!entries[0].isIntersecting) return;
  obs.disconnect();
  data.forEach(function(d,i) {
    var pct = ((d.auc - minAUC)/(maxAUC - minAUC)*100).toFixed(1);
    setTimeout(function() {
      document.querySelectorAll('.rung')[i].classList.add('show');
      setTimeout(function() { document.getElementById('bar'+i).style.width = pct+'%'; }, 150);
    }, i*280);
  });
}, {threshold:0.3});
obs.observe(ladder);
</script>
</body>
</html>"""


def render():
    n = numbers()
    b4 = n["block4_supervised"]

    st.markdown('<div id="block4" style="scroll-margin-top:80px;height:0;overflow:hidden;"></div>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TAG}">Block 4 — Supervised Learning</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TTL}">Teaching a Machine to Read a Race</span>', unsafe_allow_html=True)
    st.markdown(
        f'<span style="{_HOOK}">{n["translations"]["walkforward"]}'
        f' Five models, each adding one more layer — from grid position alone up to XGBoost '
        f'with full features. Each was tested only on seasons it had never seen.</span>',
        unsafe_allow_html=True,
    )

    ladder_data = [{"id": k, "auc": v, "label": b4["labels"][k]} for k, v in b4["auc"].items()]
    ladder_html = LADDER_HTML.replace("LADDER_DATA_PLACEHOLDER", json.dumps(ladder_data))

    cols = st.columns([2, 1])
    with cols[0]:
        components.html(ladder_html, height=300, scrolling=False)
    with cols[1]:
        st.markdown(
            f'<div class="card teal-accent reveal">'
            f'<div style="font-family:JetBrains Mono,monospace;font-weight:700;font-size:2.8rem;color:#00D2BE;line-height:1;letter-spacing:-1px">{b4["auc"]["M4"]}</div>'
            f'<div class="stat-label">Best AUC (M4 XGBoost)</div>'
            f'<div class="stat-caption">Walk-forward validation — trained on past seasons, tested on future ones.</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="card reveal" style="margin-top:.8rem">'
            f'<div style="font-family:JetBrains Mono,monospace;font-weight:700;font-size:2rem;color:#9A9AA8;line-height:1">+{b4["delta_M2_M1"]:.4f}</div>'
            f'<div class="stat-label">Strategy lift (M2 − M1)</div>'
            f'<div class="stat-caption">Adding strategy variables to the car-quality baseline.</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<span style="font-size:1rem;font-weight:700;color:#E8E8E8;margin:1.2rem 0 .3rem;'
        f'font-family:\'Titillium Web\',sans-serif;display:block;">What drives the model\'s predictions?</span>',
        unsafe_allow_html=True,
    )
    # Donut — 3 clean slices summing to exactly 1.0
    other = round(1.0 - b4["car_quality_share"] - b4["strategic_alpha"], 4)
    fig = go.Figure(go.Pie(
        labels=["Car quality", "Strategy (α)", "Other / unexplained"],
        values=[b4["car_quality_share"], b4["strategic_alpha"], other],
        hole=.55,
        marker_colors=["#E10600", "#00D2BE", "#3A3A50"],
        textinfo="label+percent",
        textfont_size=13,
    ))
    fig.update_layout(
        showlegend=False, height=320,
        annotations=[dict(
            text=f'<b>{b4["strategic_alpha"]*100:.1f}%</b><br><span style="font-size:11px">Strategy</span>',
            x=0.5, y=0.5, font_size=18, showarrow=False,
        )],
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        f'<div class="card reveal" style="margin-top:.5rem">'
        f'Pooled diagnostics n = <b style="font-family:JetBrains Mono,monospace">{b4["pooled_n"]:,}</b> · '
        f'Walk-forward: trained on past seasons, tested on the next — never random CV.'
        f'</div>',
        unsafe_allow_html=True,
    )

    col_a, col_b = st.columns(2)
    with col_a:
        p = os.path.join(_PLOTS, "B4_02_shap_beeswarm.png")
        if os.path.exists(p):
            st.image(p, caption="SHAP beeswarm — feature contributions to XGBoost predictions. Each dot = one race observation. Red = high feature value; blue = low.", use_container_width=True)
    with col_b:
        p = os.path.join(_PLOTS, "B4_01_model_comparison.png")
        if os.path.exists(p):
            st.image(p, caption="Walk-forward AUC by model tier. M0 = grid position only; M4 = full XGBoost with strategy features. Each point = one test-season fold.", use_container_width=True)
