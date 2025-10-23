# CONTENT SCOPE
The slide content must revolving around product management alone, do NOT drift away from this topic.

----------------
#**Encoding Safety:** Do **not** use PowerShell `Get-Content`/`Set-Content`, `-replace`, or ad-hoc byte conversion for editing project files. They default to CP1252 and corrupt UTF-8 files (e.g., `<?php`, umlauts).

All coding agents must:
- Read and comply with this file before making any edits.
- Use `apply_patch` or Python (`python - <<PY  PY`) with explicit UTF-8 read/write for every file modification.
- Treat attempts to rely on PowerShell text utilities as violations; stop immediately and switch to an approved method.
- Escalate to the maintainer if neither `apply_patch` nor Python is available.

