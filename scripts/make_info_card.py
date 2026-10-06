from pathlib import Path

OUTPUT = Path("info-card.svg")

W = 840
H = 880

BG = "#0d1117"
FRAME = "#30363d"
MUTED = "#7d8590"
INK = "#e6edf3"
GREEN = "#39d353"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{W}" height="{H}" viewBox="0 0 {W} {H}"
font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">

<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#111722"/>
        <stop offset="1" stop-color="{BG}"/>
    </linearGradient>
</defs>

<style>
    .reveal {{
        opacity: 0;
        animation: reveal 0.5s ease-out forwards;
    }}

    @keyframes reveal {{
        from {{
            opacity: 0;
            transform: translateY(12px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
</style>

<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}"
      rx="12" fill="none" stroke="{FRAME}"/>

<line x1="0" y1="30" x2="{W}" y2="30" stroke="{FRAME}"/>

<circle cx="40" cy="15" r="5" fill="#ff5f56"/>
<circle cx="56" cy="15" r="5" fill="#ffbd2e"/>
<circle cx="72" cy="15" r="5" fill="#27c93f"/>

<text x="{W/2}" y="19"
      fill="{MUTED}"
      font-size="12"
      text-anchor="middle">
    anas@github: ~$ ./profile.sh
</text>

<text x="40" y="105"
      fill="{MUTED}"
      font-size="22"
      class="reveal"
      style="animation-delay:0.2s">
    $ whoami
</text>

<text x="40" y="175"
      fill="{GREEN}"
      font-size="48"
      font-weight="700"
      class="reveal"
      style="animation-delay:0.4s">
    Anas Khan
</text>

<text x="40" y="250"
      fill="{INK}"
      font-size="28"
      class="reveal"
      style="animation-delay:0.6s">
    AI/ML Enthusiast
</text>

<text x="40" y="292"
      fill="{MUTED}"
      font-size="24"
      class="reveal"
      style="animation-delay:0.75s">
    Data Science
</text>

<line x1="40" y1="360" x2="800" y2="360"
      stroke="{FRAME}"/>

<text x="40" y="425"
      fill="{MUTED}"
      font-size="22"
      class="reveal"
      style="animation-delay:0.9s">
    $ stack
</text>

<text x="40" y="475"
      fill="{INK}"
      font-size="25"
      class="reveal"
      style="animation-delay:1.05s">
    Python · Pandas · NumPy
</text>

<text x="40" y="520"
      fill="{INK}"
      font-size="25"
      class="reveal"
      style="animation-delay:1.2s">
    Scikit-learn · Flask · SQL
</text>

<text x="40" y="595"
      fill="{MUTED}"
      font-size="22"
      class="reveal"
      style="animation-delay:1.4s">
    $ exploring
</text>

<text x="40" y="647"
      fill="{INK}"
      font-size="25"
      class="reveal"
      style="animation-delay:1.55s">
    RAG · LLMs · AI Applications
</text>

<line x1="0" y1="820" x2="{W}" y2="820"
      stroke="{FRAME}"/>

<text x="40" y="855"
      fill="{MUTED}"
      font-size="16">
    anas@github:~$ <tspan fill="{INK}">_</tspan>
</text>

</svg>
"""

OUTPUT.write_text(svg, encoding="utf-8")

print(f"Created {OUTPUT}")
