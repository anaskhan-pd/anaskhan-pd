from pathlib import Path


OUTPUT = Path("info-card.svg")

lines = [
    ("Anas Khan", "name"),
    ("AI/ML Enthusiast", "role"),
    ("Data Science", "role"),
    ("", "space"),
    ("Python · Pandas · NumPy", "stack"),
    ("Scikit-learn · Flask · SQL", "stack"),
    ("", "space"),
    ("RAG · LLMs · AI Applications", "explore"),
]


def escape_xml(text):
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def main():
    width = 520
    line_height = 28
    padding = 30

    height = padding * 2 + len(lines) * line_height

    svg = [
        f'''<svg xmlns="http://www.w3.org/2000/svg"
        width="{width}"
        height="{height}"
        viewBox="0 0 {width} {height}">''',

        """
        <style>
            .terminal {
                font-family: monospace;
                fill: #666666;
            }

            .name {
                font-size: 25px;
                font-weight: bold;
                fill: #444444;
            }

            .role {
                font-size: 18px;
            }

            .stack {
                font-size: 17px;
            }

            .explore {
                font-size: 17px;
            }

            .line {
                opacity: 0;
                animation: appear 0.5s ease-out forwards;
            }

            @keyframes appear {
                from {
                    opacity: 0;
                    transform: translateX(-10px);
                }

                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }
        </style>
        """
    ]

    y = padding + 22

    animation_index = 0

    for text, kind in lines:

        if kind == "space":
            y += 10
            continue

        delay = animation_index * 0.12

        svg.append(
            f'''
            <text
                x="{padding}"
                y="{y}"
                class="terminal {kind} line"
                style="animation-delay:{delay:.2f}s">
                {escape_xml(text)}
            </text>
            '''
        )

        y += line_height
        animation_index += 1

    svg.append("</svg>")

    OUTPUT.write_text("\n".join(svg), encoding="utf-8")

    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()
