import os
from pathlib import Path


def get_cli_arguments(args: list[str]) -> tuple[Path, Path, int, int]:
    if (len(args) != 5):
        raise ValueError("Format: python3 -m src.main <map input> <map output> <key count> <generation type>")

    if args[3] not in ("4", "7"):
        raise ValueError("Invalid key count: 4 or 7")

    if args[4] not in ("1", "2", "3", "4", "5"):
        raise ValueError("Invalid generation type: 1: stream, 2: light chordstream, 3: dense chordstream")

    map_path = Path(args[1])
    new_map_path = Path(args[2])
    key_count = int(args[3])
    generation_type = int(args[4])

    if not os.path.isfile(map_path) or not str(map_path).endswith(".osu"):
        raise ValueError("Invalid input, need .osu file")

    if not os.path.isdir(new_map_path.parent):
        raise ValueError("Output directory does not exist")

    # commented for debugging
    # if os.path.exists(new_map_path):
    #     raise ValueError("File exists at output path")

    return map_path, new_map_path, key_count, generation_type
