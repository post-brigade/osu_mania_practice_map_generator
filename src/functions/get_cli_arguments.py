from multiprocessing import Value
import os
from pathlib import Path

from .normalize_path import normalize_path


def get_cli_arguments(args: list[str]) -> tuple[Path, int, int]:
    if (len(args) not in (4, 5)):
        raise ValueError("Format: python3 -m src.main <key count> <generation type> <map input> <(optional) density string>")

    if args[1] not in ("4", "7"):
        raise ValueError("Invalid key count: not 4 or 7")

    if args[2] not in ("1", "2", "3", "4", "5"):
        raise ValueError("Invalid density option: not 1, 2, 3, 4, or 5")

    if len(args) == 5 and args[1] != "7":
        raise ValueError("Density string only for 7k")

    if len(args) == 5 and len(args[4]) != 5:
        raise ValueError("Invalid density string format: 5 numbers, choosing chord size every 16, 8, 4, 2, and 1 note(s). must be at least 1")

    chord_sizes: list[int] = []

    for num in args[4]:
        chord_sizes.append(int(num))

    if max(
        chord_sizes[4] + chord_sizes[0],
        chord_sizes[4] + chord_sizes[1],
        chord_sizes[4] + chord_sizes[2],
        chord_sizes[4] + chord_sizes[3]
    ) > 7:
      raise ValueError("Not enough columns for chosen chord sizes")

    chord_tuples: list[tuple[int, int]] = []
    beat = 16
    for i in range(5):
        chord_tuples.append((beat, chord_sizes[i] ))
        beat //= 2
    print(chord_tuples)

    map_path = normalize_path(args[3])
    map_path = Path(map_path)
    key_count = int(args[1])
    generation_type = int(args[2])

    if not os.path.isfile(map_path) or not str(map_path).endswith(".osu"):
        raise ValueError("Invalid input, need .osu file")

    return map_path, key_count, generation_type
