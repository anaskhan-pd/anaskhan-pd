import json
from pathlib import Path

import requests


USERNAME = "anaskhan-pd"
OUTPUT = Path("data/contributions.json")


def main():
    url = f"https://github.com/users/{USERNAME}/contributions"

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )

    response.raise_for_status()

    html = response.text

    # Save the raw HTML temporarily so we can inspect it if GitHub
    # changes its contribution-page structure.
    Path("data/contributions.html").write_text(
        html,
        encoding="utf-8",
    )

    print(f"Downloaded GitHub contribution calendar for {USERNAME}")
    print(f"Saved raw HTML to {Path('data/contributions.html')}")


if __name__ == "__main__":
    main()
