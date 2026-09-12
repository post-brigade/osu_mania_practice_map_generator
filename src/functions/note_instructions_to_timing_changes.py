import copy
import math

from src.classes import TimingPoint

from .create_timing_point import create_timing_point


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

        if sorted_timing_points[i].is_bpm_change:
            insert_bpm_timing_point(sorted_timing_points[i], final_timing_points)

        elif sorted_timing_points[i].is_start_stop:
            insert_start_stop_timing_point(sorted_timing_points[i], final_timing_points)

        else:
            insert_timing_point(sorted_timing_points[i], final_timing_points)

    return final_timing_points


def create_bpm_timing_point(bpm_change: tuple[int, float]) -> TimingPoint:
    if bpm_change[0] == 3:
        time_mult = .5
    elif bpm_change[0] == 4:
        time_mult = 2
    else:
        raise ValueError("invalid bpm change tuple")

    new_bpm_change = create_timing_point([str(bpm_change[1]), "1", "1", "1", "1", "1", "1", "1"]
    )
    new_bpm_change.is_bpm_change = True
    new_bpm_change.time_multiplier = time_mult

    return new_bpm_change


def create_start_stop_timing_point(start_stop: tuple[int, float]) -> TimingPoint:
    new_start_stop = create_timing_point([str(start_stop[1]), "1", "1", "1", "1", "1", "1", "1"])
    new_start_stop.is_start_stop = True

    return new_start_stop


def insert_bpm_timing_point(bpm_change_point: TimingPoint, final_timing_points: list[TimingPoint]):
    time = bpm_change_point.time
    multiplier = bpm_change_point.time_multiplier

    if math.isclose(bpm_change_point.time, final_timing_points[-1].time, abs_tol=0.001):
        final_timing_points[-1].is_bpm_change = True
        final_timing_points[-1].time_multiplier *= multiplier
        final_timing_points[-1].update_beat_length()

        return

    bpm_change_point = copy.copy(final_timing_points[-1])
    bpm_change_point.time = time
    bpm_change_point.is_start_stop = False
    bpm_change_point.is_bpm_change = True
    bpm_change_point.time_multiplier = multiplier * final_timing_points[-1].time_multiplier
    bpm_change_point.update_beat_length()

    final_timing_points.append(bpm_change_point)


def insert_start_stop_timing_point(start_stop_point: TimingPoint, final_timing_points: list[TimingPoint]):
    time = start_stop_point.time

    if math.isclose(start_stop_point.time, final_timing_points[-1].time, abs_tol=0.001):
        final_timing_points[-1].is_start_stop = True
        final_timing_points[-1].generate_notes = not final_timing_points[-1].generate_notes

        return

    start_stop_point = copy.copy(final_timing_points[-1])
    start_stop_point.time = time
    start_stop_point.is_start_stop = True
    start_stop_point.is_bpm_change = False
    start_stop_point.generate_notes = not final_timing_points[-1].generate_notes

    final_timing_points.append(start_stop_point)


def insert_timing_point(timing_point: TimingPoint, final_timing_points: list[TimingPoint]):
    if math.isclose(timing_point.time, final_timing_points[-1].time, abs_tol=0.001):
        is_start_stop = final_timing_points[-1].is_start_stop
        is_bpm_change = final_timing_points[-1].is_bpm_change
        final_timing_points[-1] = timing_point
        final_timing_points[-1].is_start_stop = is_start_stop
        final_timing_points[-1].is_bpm_change = is_bpm_change
    else:
        timing_point.time_multiplier = final_timing_points[-1].time_multiplier
        timing_point.generate_notes = final_timing_points[-1].generate_notes
        timing_point.update_beat_length()

        final_timing_points.append(timing_point)
