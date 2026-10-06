from pathlib import Path

from PIL import Image, ImageOps


INPUT = Path("source-prepped.png")
OUTPUT = Path("anaskhan-ascii.svg")

# Bright -> dark
RAMP = " .`:-=+*cs#%@"

# Character grid
WIDTH = 100
CHAR_ASPECT = 0.5

# SVG appearance
FONT_SIZE = 10
LINE_HEIGHT = 10
FILL = "#666666"


def brightness_to_char(value):
    index = int((255 - value) / 255 * (len(RAMP) - 1))
    return RAMP[index]


def main():
    image = Image.open(INPUT).convert("L")

    # Preserve the portrait's proportions while compensating
    # for characters being taller than they are wide.
    aspect = image.height / image.width
    height = max(1, int(WIDTH * aspect * CHAR_ASPECT))

    image = image.resize((WIDTH, height))

    pixels = image.load()

    rows = []

    for y in range(height):
        row = ""

        for x in range(WIDTH):
            row += brightness_to_char(pixels[x, y])

        rows.append(row.rstrip())

    svg_width = WIDTH * FONT_SIZE
    svg_height = height * LINE_HEIGHT

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{svg_width}" height="{svg_height}" '
        f'viewBox="0 0 {svg_width} {svg_height}">',
        "<style>",
        """
        .ascii-row {
            font-family: monospace;
            font-size: 10px;
            fill: #666666;
            white-space: pre;
        }

        .row {
            animation: reveal 0.55s ease-out forwards;
            clip-path: inset(0 100% 0 0);
        }

        @keyframes reveal {
            from {
                clip-path: inset(0 100% 0 0);
            }
            to {
                clip-path: inset(0 0 0 0);
            }
        }
        """,
        "</style>",
    ]

    for y, row in enumerate(rows):
        delay = y * 0.025
        baseline = (y + 1) * LINE_HEIGHT

        svg.append(
            f'<g class="row" style="animation-delay:{delay:.3f}s">'
        )

        svg.append(
            f'<text class="ascii-row" '
            f'x="0" y="{baseline}">'
            f'{escape_xml(row)}'
            f'</text>'
        )

        svg.append("</g>")

    svg.append("</svg>")

    OUTPUT.write_text("\n".join(svg), encoding="utf-8")

    print(f"Created {OUTPUT}")
    print(f"Grid: {WIDTH} × {height}")
    print(f"SVG size: {svg_width} × {svg_height}")


def escape_xml(text):
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


if __name__ == "__main__":
    main()
