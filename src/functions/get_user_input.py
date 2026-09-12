import os
from pathlib import Path

from .normalize_path import normalize_path


def get_user_input() -> tuple[Path, Path, int, int]:

    key_count = int(input("Enter key count: 4 or 7:\n"))

    if key_count == 7:
        density = int(input("Choose density:\n\t"
            "1: stream\n\t"
            "2: light chordsream: 2 note chords\n\t"
            "3: light chordstream: 4 note chords\n\t"
            "4: dense chordstream: 2 note chords\n\t"
            "5: dense chordstream: 3 and 4 note chords\n"
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

    new_path_input = input("choose output location:\n")
    new_map_path = normalize_path(new_path_input)

    if not map_path.is_file() or map_path.suffix != ".osu":
        raise ValueError("Invalid input, need .osu file")

    if new_map_path.suffix != ".osu":
        raise ValueError("Invalid output, should be .osu file")

    if not new_map_path.parent.is_dir():
        raise ValueError("Output directory does not exist")

    # commented for debugging
    # if os.path.exists(new_map_path):
    #     raise ValueError("File exists at output path")


    return map_path, new_map_path, key_count, density
