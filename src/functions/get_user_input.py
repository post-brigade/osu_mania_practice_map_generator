import os
from pathlib import Path

from .normalize_path import normalize_path


def get_user_input() -> tuple[Path, int, int]:

    key_count = int(input("Enter key count: 4 or 7:\n"))

    if key_count == 7:
        density = int(input("Choose density:\n\t"
            "1: stream\n\t"
            "2: light chordstream\n\t"
            "3: less light chordstream\n\t"
            "4: dense-ish chordstream\n\t"
            "5: dense chordstream\n"
        ))
    elif key_count == 4:
        density = int(input("Choose density:\n\t"
            "1: stream\n\t"
            "2: light jumpstream\n\t"
            "3: dense jumpstream\n\t"
            "4: light handstream\n\t"
            "5: dense handstream\n"
        ))
    else:
        raise ValueError("Invalid key count")

    if density not in (1, 2, 3, 4, 5):
        raise ValueError("Invalid density")

    path_input = input("choose target map:\n")
    map_path = normalize_path(path_input)

    if not map_path.is_file() or map_path.suffix != ".osu":
        raise ValueError("Invalid input, need .osu file")

    # commented for debugging
    # if os.path.exists(new_map_path):
    #     raise ValueError("File exists at output path")


    return map_path, key_count, density
