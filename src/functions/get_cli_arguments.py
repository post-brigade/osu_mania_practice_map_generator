import os
from pathlib import Path


def get_cli_arguments(args: list[str]) -> tuple[Path, int, int]:
    if (len(args) != 4):
        raise ValueError("Format: python3 -m src.main <key count> <generation type> <map input>")

    if args[1] not in ("4", "7"):
        raise ValueError("Invalid key count: not  4 or 7")

    if args[2] not in ("1", "2", "3", "4", "5"):
        raise ValueError("Invalid generation type: not 1, 2, 3, 4, or 5")

    map_path = Path(args[3])
    key_count = int(args[1])
    generation_type = int(args[2])

    if not os.path.isfile(map_path) or not str(map_path).endswith(".osu"):
        raise ValueError("Invalid input, need .osu file")

    return map_path, key_count, generation_type
