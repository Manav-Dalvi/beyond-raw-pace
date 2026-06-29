import streamlit as st
import streamlit.components.v1 as components
import json, os
import plotly.graph_objects as go
from data_loader import numbers

_PLOTS = os.path.join(os.path.dirname(__file__), "..", "assets", "outputs", "plots")

_TAG  = "color:#E10600;text-transform:uppercase;letter-spacing:.25em;font-size:.75rem;font-weight:700;margin-bottom:.4rem;font-family:'Titillium Web',sans-serif;display:block;"
_TTL  = "font-size:clamp(1.8rem,4vw,3rem);font-weight:900;color:#E8E8E8;letter-spacing:-.02em;line-height:1.1;margin-bottom:.8rem;font-family:'Titillium Web',sans-serif;display:block;"
_HOOK = "font-size:1.1rem;color:#9A9AA8;max-width:680px;line-height:1.6;margin-bottom:1.8rem;font-family:'Titillium Web',sans-serif;display:block;"


def render():
    n = numbers()
    b1 = n["block1_unsupervised"]

    st.markdown('<div id="block1" style="scroll-margin-top:80px;height:0;overflow:hidden;"></div>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TAG}">Block 1 — Circuit Structure</span>', unsafe_allow_html=True)
    st.markdown(f'<span style="{_TTL}">Tracks Have Personalities</span>', unsafe_allow_html=True)
    st.markdown(
        f'<span style="{_HOOK}">{n["translations"]["clusters"]}'
        f' PCA + K-Means clustering (k={b1["k"]}) on {n["scale"]["circuits_clustered"]} circuits '
        f'reveals three distinct strategic archetypes.</span>',
        unsafe_allow_html=True,
    )

    colors = ["#E10600", "#FFF200", "#00D2BE"]
    icons = ["📍", "⚖️", "🌀"]
    cols = st.columns(3)
    for i, (col, arc) in enumerate(zip(cols, b1["archetypes"])):
        with col:
            st.markdown(
                f'<div class="card reveal" style="border-top:3px solid {colors[i]}">'
                f'<div style="font-size:1.5rem;margin-bottom:.4rem">{icons[i]}</div>'
                f'<div style="font-weight:700;color:{colors[i]};font-size:1.05rem">{arc["plain"]}</div>'
                f'<div style="color:#9A9AA8;font-size:.85rem;margin:.4rem 0">{arc["name"]}</div>'
                f'<div style="font-family:JetBrains Mono,monospace;font-size:1.2rem;color:#E8E8E8">'
                f'{arc["n"]} circuits</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

    st.markdown(
        f'<div class="card reveal" style="margin-top:1rem">'
        f'<div style="color:#9A9AA8;font-size:.85rem;margin-bottom:.6rem;text-transform:uppercase;letter-spacing:.15em">Cluster quality</div>'
        f'<span style="margin-right:2rem">Silhouette: '
        f'<b style="font-family:JetBrains Mono,monospace;color:#00D2BE">{b1["silhouette"]}</b></span>'
        f'<span>K-Means vs Hierarchical ARI: '
        f'<b style="font-family:JetBrains Mono,monospace;color:#00D2BE">{b1["ari_kmeans_vs_hier"]:.3f}</b>'
        f' (identical partition)</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    circuits_path = os.path.join(os.path.dirname(__file__), "..", "assets", "circuits.json")
    if os.path.exists(circuits_path):
        with open(circuits_path, encoding="utf-8") as f:
            circuits = json.load(f)

        colors_map = {"Strategy decides here": "#E10600", "All-rounders": "#FFF200", "Chaos-friendly": "#00D2BE"}
        fig = go.Figure()
        for arc in b1["archetypes"]:
            subset = [c for c in circuits if c.get("archetype") == arc["name"]]
            if not subset:
                continue
            color = colors_map.get(arc["plain"], "#E8E8E8")
            fig.add_trace(go.Scatter(
                x=[c["pc1"] for c in subset], y=[c["pc2"] for c in subset],
                mode="markers+text", name=arc["plain"],
                marker=dict(color=color, size=12, opacity=.85, line=dict(color="#15151E", width=1)),
                text=[c["circuit"] for c in subset], textposition="top center",
                textfont=dict(size=9, color="#9A9AA8"),
                hovertemplate="<b>%{text}</b><br>β = %{customdata:.3f}<extra></extra>",
                customdata=[c.get("beta", 0) for c in subset],
            ))
        fig.update_layout(title="Circuit archetypes (PCA)", xaxis_title="PC1", yaxis_title="PC2", height=380)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Select a circuit to explore its profile:**")
        track_html_path = os.path.join(os.path.dirname(__file__), "..", "components", "track_map.html")
        with open(track_html_path, encoding="utf-8") as f:
            track_html = f.read()

        plain_lookup = {a["name"]: a["plain"] for a in b1["archetypes"]}
        enriched = [dict(c, plain=plain_lookup.get(c.get("archetype", ""), c.get("archetype", ""))) for c in circuits]
        data_script = f"<script>window.CIRCUITS_DATA = {json.dumps(enriched)};</script>"
        track_html = track_html.replace("<body>", "<body>" + data_script)
        components.html(track_html, height=340, scrolling=True)
    else:
        st.info("Add `assets/circuits.json` (exported from the notebook) to enable the interactive circuit explorer.")

    st.markdown(
        '<div style="display:flex;gap:1rem;margin-top:1.2rem;flex-wrap:wrap">',
        unsafe_allow_html=True,
    )
    col_a, col_b = st.columns(2)
    with col_a:
        p = os.path.join(_PLOTS, "b1_07_elasticity_bars.png")
        if os.path.exists(p):
            st.image(p, caption="Penalty-cost elasticity (β) per circuit — ranked. Error bars = 95% CI from OLS. Red = high-cost (β > 0.75), yellow = moderate, teal = low-cost.", use_container_width=True)
    with col_b:
        p = os.path.join(_PLOTS, "b1_05_biplot.png")
        if os.path.exists(p):
            st.image(p, caption="Circuit biplot (PC1 × PC2). Colour = cluster archetype. PC1 captures the overtaking / dominance dimension; PC2 captures pace spread.", use_container_width=True)
