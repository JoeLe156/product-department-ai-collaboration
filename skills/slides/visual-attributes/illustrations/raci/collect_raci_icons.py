import io
import os
import sys
from urllib.request import urlopen

BASE = "https://unpkg.com/lucide-static@latest/icons"
ICONS = {
    "pm-briefcase.svg": "briefcase.svg",      # Product Manager
    "ai-bot.svg": "bot.svg",                  # AI Agent
    "design-pen-tool.svg": "pen-tool.svg",    # Design
    "eng-code-2.svg": "code-2.svg",          # Engineering
}

def fetch(url: str) -> bytes:
    with urlopen(url) as r:
        return r.read()

def main():
    outdir = os.path.dirname(__file__)
    for out_name, icon_name in ICONS.items():
        url = f"{BASE}/{icon_name}"
        data = fetch(url)
        path = os.path.join(outdir, out_name)
        with io.open(path, 'wb') as f:
            f.write(data)
        print("Saved", out_name)
    print("Done.")

if __name__ == "__main__":
    sys.exit(main())

