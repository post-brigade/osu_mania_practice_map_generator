import re
import subprocess
from pathlib import Path


def normalize_path(raw_input: str) -> Path:
    cleaned = raw_input.strip().strip("'\"")

    if is_windows_path(cleaned):
        result = subprocess.run(
            ["wslpath", "-u", cleaned],
            capture_output=True,
            text=True,
            check=True
        )
        cleaned = result.stdout.strip()

    return Path(cleaned)


def is_windows_path(path: str) -> bool:
    clean_path = path.strip().strip("'\"")
    return bool(re.match(r"^[a-zA-Z]:[\\/]", clean_path) or clean_path.startswith("\\\\"))
