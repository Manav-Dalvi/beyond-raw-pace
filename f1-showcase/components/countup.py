import streamlit.components.v1 as components

COUNTUP_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Titillium+Web:wght@400;700&display=swap" rel="stylesheet">
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:transparent; display:flex; align-items:center; justify-content:{ALIGN}; }
  .wrap { text-align:{TEXT_ALIGN}; }
  .num {
    font-family:'JetBrains Mono',monospace; font-weight:700;
    font-size:{SIZE}; color:{COLOR}; line-height:1; letter-spacing:-1px;
  }
  .label {
    font-family:'Titillium Web',sans-serif; text-transform:uppercase;
    letter-spacing:.18em; color:#9A9AA8; font-size:.75rem; margin-top:.4rem;
  }
  .caption {
    font-family:'Titillium Web',sans-serif; color:#9A9AA8;
    font-size:.9rem; margin-top:.5rem; max-width:280px; line-height:1.4;
  }
</style>
</head>
<body>
<div class="wrap">
  <div class="num" id="counter">{PREFIX}0{SUFFIX}</div>
  <div class="label">{LABEL}</div>
  {CAPTION_HTML}
</div>
<script>
  const target = {TARGET};
  const prefix = "{PREFIX}";
  const suffix = "{SUFFIX}";
  const decimals = {DECIMALS};
  const duration = {DURATION};
  const el = document.getElementById('counter');
  let start = null;
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }
  function animate(ts) {
    if (!start) start = ts;
    const progress = Math.min((ts - start) / duration, 1);
    const val = target * easeOut(progress);
    el.textContent = prefix + val.toFixed(decimals) + suffix;
    if (progress < 1) requestAnimationFrame(animate);
  }
  const obs = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      requestAnimationFrame(animate);
      obs.disconnect();
    }
  }, {threshold: 0.5});
  obs.observe(document.getElementById('counter'));
</script>
</body>
</html>
"""


def countup(
    value: float,
    label: str = "",
    prefix: str = "",
    suffix: str = "",
    decimals: int = 0,
    color: str = "#E8E8E8",
    size: str = "clamp(2.5rem,7vw,4.5rem)",
    caption: str = "",
    height: int = 140,
    align: str = "center",
):
    caption_html = f'<div class="caption">{caption}</div>' if caption else ""
    text_align = "center" if align == "center" else "left"
    flex_align = "center" if align == "center" else "flex-start"

    html = COUNTUP_TEMPLATE.replace("{TARGET}", str(value))
    html = html.replace("{PREFIX}", prefix)
    html = html.replace("{SUFFIX}", suffix)
    html = html.replace("{DECIMALS}", str(decimals))
    html = html.replace("{DURATION}", "1200")
    html = html.replace("{LABEL}", label)
    html = html.replace("{COLOR}", color)
    html = html.replace("{SIZE}", size)
    html = html.replace("{CAPTION_HTML}", caption_html)
    html = html.replace("{ALIGN}", flex_align)
    html = html.replace("{TEXT_ALIGN}", text_align)

    components.html(html, height=height, scrolling=False)
