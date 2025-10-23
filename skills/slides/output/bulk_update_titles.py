import io
import os
import re

BASE_DIR = os.path.dirname(__file__)

TITLE_PREFIX_RE = re.compile(r"^#\s+Slide\s+\d+\s+[—-]\s+", re.UNICODE)
AS_OF_RE = re.compile(r"\s*\(as of Oct 2025\)\s*$", re.UNICODE)


def process_file(path: str):
    name = os.path.basename(path)
    try:
        idx = int(os.path.splitext(name)[0].split('-')[1])
    except Exception:
        idx = 0

    with io.open(path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    if not lines:
        return False

    original_title = lines[0]
    # Remove leading markdown and "Slide N —" prefix
    if original_title.startswith('#'):
        t = original_title
        t = TITLE_PREFIX_RE.sub('# ', t)
        # If the line still starts with '# Slide' (different dash), normalize again
        if t.startswith('# Slide '):
            t = re.sub(r"^#\s+Slide\s+\d+\s+[-–—]\s+", '# ', t)
    else:
        t = '# ' + original_title.lstrip('# ').strip()

    # For slides 2+, remove "(as of Oct 2025)" at end of title
    if idx >= 2:
        t = AS_OF_RE.sub('', t)

    changed = t != original_title
    lines[0] = t

    # For slides 2+, insert subtitle line after the H1
    if idx >= 2:
        subtitle = 'Trending PM workflows'
        # Insert only if the immediate next non-empty line isn't already the subtitle
        insert_pos = 1
        if len(lines) > 1:
            next_line = lines[1].strip()
            if next_line.lower() != subtitle.lower():
                lines.insert(insert_pos, subtitle)
                changed = True
        else:
            lines.append(subtitle)
            changed = True

    if changed:
        with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(lines) + '\n')
    return changed


def main():
    changed_any = False
    for fname in sorted(os.listdir(BASE_DIR)):
        if not fname.startswith('slides-') or not fname.endswith('.md'):
            continue
        path = os.path.join(BASE_DIR, fname)
        if process_file(path):
            print('Updated', fname)
            changed_any = True
    if not changed_any:
        print('No changes needed')


if __name__ == '__main__':
    main()

