import re
from pathlib import Path
from html import escape


INPUT = Path("data/contributions.html")
OUTPUT = Path("contrib-heatmap.svg")

# GitHub contribution colors
COLORS = {
    0: "#ebedf0",
    1: "#9be9a8",
    2: "#40c463",
    3: "#30a14e",
    4: "#216e39",
}


def parse_contributions():
    html = INPUT.read_text(encoding="utf-8")

    pattern = re.compile(
        r'data-date="([^"]+)"[^>]*data-level="([0-4])"'
    )

    contributions = []

    for date, level in pattern.findall(html):
        contributions.append(
            {
                "date": date,
                "level": int(level),
            }
        )

    return contributions


def main():
    contributions = parse_contributions()

    if not contributions:
        raise RuntimeError("No contribution data found.")

    # GitHub gives us the days in calendar order.
    # We render them in 53 columns × 7 rows.
    weeks = []

    for i in range(0, len(contributions), 7):
        weeks.append(contributions[i:i + 7])

    cell = 11
    gap = 3

    width = len(weeks) * (cell + gap)
    height = 7 * (cell + gap)

    svg = [
        f'''<svg xmlns="http://www.w3.org/2000/svg"
        width="{width}"
        height="{height}"
        viewBox="0 0 {width} {height}">''',

        """
        <style>
            .cell {
                opacity: 0;
                transform: scale(0.7);
                transform-origin: center;
                animation: appear 0.25s ease-out forwards;
            }

            @keyframes appear {
                from {
                    opacity: 0;
                    transform: scale(0.7);
                }

                to {
                    opacity: 1;
                    transform: scale(1);
                }
            }
        </style>
        """
    ]

    index = 0

    for x, week in enumerate(weeks):

        for y, item in enumerate(week):

            level = item["level"]
            color = COLORS[level]

            px = x * (cell + gap)
            py = y * (cell + gap)

            delay = index * 0.012

            svg.append(
                f'''
                <rect
                    class="cell"
                    x="{px}"
                    y="{py}"
                    width="{cell}"
                    height="{cell}"
                    rx="2"
                    fill="{color}"
                    style="animation-delay:{delay:.3f}s">
                    <title>
                        {escape(item["date"])}
                    </title>
                </rect>
                '''
            )

            index += 1

    svg.append("</svg>")

    OUTPUT.write_text(
        "\n".join(svg),
        encoding="utf-8",
    )

    print(f"Created {OUTPUT}")
    print(f"Contribution cells: {len(contributions)}")
    print(f"SVG size: {width} × {height}")


if __name__ == "__main__":
    main()
