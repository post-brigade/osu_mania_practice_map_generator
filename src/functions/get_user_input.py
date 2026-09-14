from pathlib import Path

from .normalize_path import normalize_path


def get_user_input() -> tuple[Path, int, int]:

    key_count = int(input("Enter key count: 4 or 7:\n"))

    if key_count == 7:
        density = int(input("Choose density:\n\t"
            "1: Stream\n\t"
            "2: Light Chordstream\n\t"
            "3: Light-ish Chordstream\n\t"
            "4: Dense-ish Chordstream\n\t"
            "5: Dense Chordstream\n"
        ))
    elif key_count == 4:
        density = int(input("Choose density:\n\t"
            "1: Stream\n\t"
            "2: Light Jumpstream\n\t"
            "3: Dense Jumpstream\n\t"
            "4: Light Handstream\n\t"
            "5: Dense Handstream\n"
        ))
    else:
        raise ValueError("Invalid key count")

    if density not in (1, 2, 3, 4, 5):
        raise ValueError("Invalid density")

    path_input = input("choose target map:\n")
    map_path = normalize_path(path_input)

    if not map_path.is_file() or map_path.suffix != ".osu":
        raise ValueError("Invalid input: need .osu file, or unexpected character in file name. i.e. \"!\"")

    return map_path, key_count, density
