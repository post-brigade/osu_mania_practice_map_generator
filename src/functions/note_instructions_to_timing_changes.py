import copy

from src.classes import TimingPoint

from .create_timing_point import create_timing_point


def create_bpm_timing_point(bpm_change: tuple[int, float]) -> TimingPoint:
    if bpm_change[0] == 3:
        time_mult = .5
    elif bpm_change[0] == 4:
        time_mult = 2
    else:
        raise ValueError("invalid bpm change tuple")

    new_bpm_change = create_timing_point(
        [
        str(bpm_change[1]),
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1"
    ]
    )
    new_bpm_change.is_bpm_change = True
    new_bpm_change.time_multiplier = time_mult

    return new_bpm_change

def create_start_stop_timing_point(start_stop: tuple[int, float]):

    new_start_stop = create_timing_point(
        [
        str(start_stop[1]),
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1"
    ]
    )
    new_start_stop.is_start_stop = True

    return new_start_stop


def note_instructions_to_timing_changes(
    timing_points: list[TimingPoint],
    instructions: list[tuple[int, float]]
) -> list[TimingPoint]:
    new_timing_points: list[TimingPoint] = []
    new_timing_points.extend(timing_points)

    for instruction in instructions:
        if instruction[0] == 1 or instruction[0] == 2:
            new_timing_point = create_start_stop_timing_point(instruction)
        elif instruction[0] == 3 or instruction[0] == 4:
            new_timing_point = create_bpm_timing_point(instruction)
        else:
            raise ValueError("Invalid instruction tuple")

        new_timing_points.append(new_timing_point)

    sorted_timing_points = sorted(new_timing_points, key = lambda change: (change.time, change.is_start_stop, change.is_bpm_change))

    final_timing_points: list[TimingPoint] = []


    for i in range(len(sorted_timing_points)):
        if i == 0:
                if sorted_timing_points[i].is_bpm_change or sorted_timing_points[i].is_start_stop:
                    raise ValueError("instruction before timing point")
                final_timing_points.append(sorted_timing_points[i])
                continue

        if i > 0 and sorted_timing_points[i].is_bpm_change:
            time = sorted_timing_points[i].time
            multiplier = sorted_timing_points[i].time_multiplier

            if sorted_timing_points[i].time == final_timing_points[-1].time:
                final_timing_points[-1].time_multiplier *= multiplier
                final_timing_points[-1].update_beat_length()
                continue

            sorted_timing_points[i] = copy.copy(final_timing_points[-1])

            sorted_timing_points[i].time = time
            sorted_timing_points[i].generate_notes = final_timing_points[-1].generate_notes
            sorted_timing_points[i].time_multiplier = multiplier * final_timing_points[-1].time_multiplier
            sorted_timing_points[i].update_beat_length()

            final_timing_points.append(sorted_timing_points[i])
            continue

        if i > 0 and sorted_timing_points[i].is_start_stop:
            time = sorted_timing_points[i].time

            if sorted_timing_points[i].time == final_timing_points[-1].time:
                final_timing_points[-1].is_start_stop = True
                final_timing_points[-1].generate_notes = not final_timing_points[-1].generate_notes
                final_timing_points[-1].update_beat_length()

                continue

            sorted_timing_points[i] = copy.copy(final_timing_points[-1])

            sorted_timing_points[i].time = time
            sorted_timing_points[i].is_start_stop = True
            sorted_timing_points[i].generate_notes = not final_timing_points[-1].generate_notes
            sorted_timing_points[i].time_multiplier = final_timing_points[-1].time_multiplier
            sorted_timing_points[i].update_beat_length()

            final_timing_points.append(sorted_timing_points[i])

            continue

        if i > 0:
            if sorted_timing_points[i].time == final_timing_points[-1].time:
                final_timing_points[-1] = sorted_timing_points[i]
            else:
                sorted_timing_points[i].time_multiplier = final_timing_points[-1].time_multiplier
                sorted_timing_points[i].generate_notes = final_timing_points[-1].generate_notes
                sorted_timing_points[i].update_beat_length()
                final_timing_points.append(sorted_timing_points[i])

    return final_timing_points
