import json
import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st
import streamlit.components.v1 as components

CARBON, CARBON2, RED = "#15151E", "#1F1F2B", "#E10600"
INK, MUTED, GRID = "#E8E8E8", "#9A9AA8", "#2A2A38"
TEAL, AMBER, PURPLE = "#00D2BE", "#FFF200", "#9B59B6"
COLORWAY = [RED, TEAL, AMBER, PURPLE, "#3498DB"]

_CSS = """
:root{
  --carbon:#15151E; --carbon-2:#1F1F2B; --f1-red:#E10600;
  --ink:#E8E8E8; --muted:#9A9AA8; --teal:#00D2BE;
  --amber:#FFF200; --purple:#9B59B6; --grid-line:#2A2A38;
}
html,body,[class*="css"]{font-family:'Titillium Web',sans-serif;}
.stApp{background:var(--carbon)!important;}
.block-container{padding-top:0!important;max-width:1100px!important;}
.card{
  background:var(--carbon-2)!important;border:1px solid var(--grid-line)!important;
  border-radius:14px!important;padding:1.4rem 1.6rem!important;margin-bottom:1rem!important;
}
.card.accent{border-top:3px solid var(--f1-red)!important;}
.card.teal-accent{border-top:3px solid var(--teal)!important;}
.card.amber-accent{border-top:3px solid var(--amber)!important;}
.stat-num{
  font-family:'JetBrains Mono',monospace!important;font-weight:700!important;
  font-size:clamp(2.5rem,7vw,5rem)!important;line-height:1!important;letter-spacing:-1px!important;
}
.stat-label{
  text-transform:uppercase!important;letter-spacing:.18em!important;
  color:var(--muted)!important;font-size:.8rem!important;margin-top:.3rem!important;
}
.stat-caption{
  color:var(--muted)!important;font-size:.95rem!important;
  margin-top:.6rem!important;line-height:1.5!important;
}
.f1-nav{
  position:sticky;top:0;z-index:100;
  background:rgba(21,21,30,.95);backdrop-filter:blur(12px);
  border-bottom:1px solid var(--grid-line);
  padding:.6rem 2rem;display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap;
}
.f1-nav a{
  color:var(--muted);text-decoration:none;font-size:.8rem;
  font-weight:600;text-transform:uppercase;letter-spacing:.1em;
  transition:color .2s;white-space:nowrap;
}
.f1-nav a:hover{color:var(--f1-red);}
.f1-nav .brand{
  font-family:'JetBrains Mono',monospace;color:var(--f1-red);
  font-weight:700;font-size:.9rem;margin-right:auto;
}
.f1-divider{height:1px;background:var(--grid-line);margin:2rem 0;}
.reveal{opacity:0;transform:translateY(20px);transition:opacity .6s ease,transform .6s ease;}
.reveal.visible{opacity:1;transform:translateY(0);}
.f1-anchor{display:block;height:0;overflow:hidden;scroll-margin-top:80px;}
#MainMenu,header,footer{visibility:hidden;}
"""

_FONTS_URL = (
    "https://fonts.googleapis.com/css2?family=Titillium+Web"
    ":wght@400;600;700;900&family=JetBrains+Mono:wght@500;700&display=swap"
)


def register_plotly_theme():
    pio.templates["f1"] = go.layout.Template(layout=dict(
        font=dict(family="Titillium Web, Inter, sans-serif", color=INK, size=15),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        colorway=COLORWAY,
        xaxis=dict(gridcolor=GRID, zerolinecolor=GRID, linecolor=GRID),
        yaxis=dict(gridcolor=GRID, zerolinecolor=GRID, linecolor=GRID),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        margin=dict(l=40, r=20, t=50, b=40),
    ))
    pio.templates.default = "f1"


def inject_global_css():
    # Inject CSS into the parent Streamlit document via a zero-height iframe script.
    # This avoids Streamlit 1.58's behaviour of rendering <style> tag text as visible content.
    css_json = json.dumps(_CSS)
    fonts_json = json.dumps(_FONTS_URL)
    script = f"""<script>
(function() {{
  var d = (window.parent || window).document;
  if (!d.getElementById('f1-global-css')) {{
    var link = d.createElement('link');
    link.rel = 'stylesheet'; link.href = {fonts_json};
    d.head.appendChild(link);
    var s = d.createElement('style');
    s.id = 'f1-global-css';
    s.textContent = {css_json};
    d.head.appendChild(s);
  }}
  // Scroll-reveal
  var obs = new IntersectionObserver(function(entries) {{
    entries.forEach(function(e) {{ if(e.isIntersecting) e.target.classList.add('visible'); }});
  }}, {{threshold:0.1}});
  function init() {{
    d.querySelectorAll('.reveal').forEach(function(el) {{ obs.observe(el); }});
  }}
  setTimeout(init, 500);
  setTimeout(init, 1500);
}})();
</script>"""
    components.html(script, height=0)
