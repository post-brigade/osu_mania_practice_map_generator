import copy

from src.classes import TimingPoint

from .create_timing_point import create_timing_point


def note_instructions_to_timing_changes(
    timing_changes: list[TimingPoint],
    bpm_instructions: list[tuple[int, float]]
) -> list[TimingPoint]:
    new_timing_changes = []
    new_timing_changes.extend(timing_changes)

    for instruction in bpm_instructions:
        if instruction[0] == 3:
            time_mult = .5
        elif instruction[0] == 4:
            time_mult = 2
        else:
            continue

        new_time_change = create_timing_point(
            [
            str(instruction[1]),
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1"
        ]
        )
        new_time_change.is_generated = True
        new_time_change.time_multiplier = time_mult
        new_timing_changes.append(new_time_change)

    sorted_time_changes = sorted(new_timing_changes, key = lambda change: (change.time, change.is_generated))


    for i in range(len(sorted_time_changes)):
        if i == 0 and sorted_time_changes[i].is_generated:
            raise ValueError("instruction before timing point")

        if i > 0 and sorted_time_changes[i].is_generated:
            time = sorted_time_changes[i].time
            multiplier = sorted_time_changes[i].time_multiplier
            sorted_time_changes[i] = copy.copy(sorted_time_changes[i - 1])
            sorted_time_changes[i].time = time
            sorted_time_changes[i].time_multiplier = multiplier * sorted_time_changes[i - 1].time_multiplier
            sorted_time_changes[i].update_beat_length()
            continue

        if i > 0:
            sorted_time_changes[i].time_multiplier = sorted_time_changes[i - 1].time_multiplier
            sorted_time_changes[i].update_beat_length()

    return sorted_time_changes
