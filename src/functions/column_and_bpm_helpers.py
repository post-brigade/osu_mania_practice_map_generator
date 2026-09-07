import random


def bpm_to_beat_length(bpm: float) -> float:
    return (1000 * 60) / bpm


def beat_length_to_bpm(beat_length: float) -> float:
    return 1 / beat_length * 1000 * 60


def x_to_column(x, key_count) -> int:
    return (x * key_count // 512) + 1


def column_to_x(column: int, key_count: int) -> int:
    if column not in range(1, key_count + 1):
        raise ValueError("Invalid column.")
    x = ((column - 1) * 512 + 256) // key_count

    return x


def random_column(banned_columns, key_count):
    allowed = [x for x in range(1, key_count + 1) if x not in banned_columns]
    if not allowed:
        raise ValueError("No valid columns")
    return random.choice(allowed)
