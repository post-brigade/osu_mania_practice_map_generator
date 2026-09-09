import copy
import math

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

def create_start_stop_timing_point(start_stop: tuple[int, float]) -> TimingPoint:
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

    # creates placeholder timing points for bpm changes and note generation flags
    for instruction in instructions:
        if instruction[0] == 1 or instruction[0] == 2:
            new_timing_point = create_start_stop_timing_point(instruction)

        elif instruction[0] == 3 or instruction[0] == 4:
            new_timing_point = create_bpm_timing_point(instruction)

        else:
            raise ValueError("Invalid instruction tuple")

        new_timing_points.append(new_timing_point)

    # sorts by time, then .is_start_stop (false first), and .is_bpm_change (false first)
    sorted_timing_points = sorted(new_timing_points, key = lambda change: (change.time, change.is_start_stop, change.is_bpm_change))

    final_timing_points: list[TimingPoint] = []

    # finalizes new timing points
    for i in range(len(sorted_timing_points)):
        if i == 0:
                if sorted_timing_points[i].is_bpm_change or sorted_timing_points[i].is_start_stop:
                    raise ValueError("instruction before timing point")

                # starts final list of timing points
                final_timing_points.append(sorted_timing_points[i])
                continue

        # checks if the timing point is bpm change
        if i > 0 and sorted_timing_points[i].is_bpm_change:

            # stores time and its multiplier in temp variables
            time = sorted_timing_points[i].time
            multiplier = sorted_timing_points[i].time_multiplier

            # if bpm changes time is same as previous timing points, applies bpm changes multiplier to previous timing point
            if math.isclose(sorted_timing_points[i].time, final_timing_points[-1].time, abs_tol=0.001):
                final_timing_points[-1].is_bpm_change = True
                final_timing_points[-1].time_multiplier *= multiplier

                #updates .active_beat_length, variable used to calculate note bpm later
                final_timing_points[-1].update_beat_length()
                continue

            # copies properties of previous timing point
            sorted_timing_points[i] = copy.copy(final_timing_points[-1])

            # updates to current timing points properties
            sorted_timing_points[i].time = time
            sorted_timing_points[i].is_start_stop = False
            sorted_timing_points[i].is_bpm_change = True

            # redundant I think
            sorted_timing_points[i].generate_notes = final_timing_points[-1].generate_notes

            # sets own time multiplier to previous time points times temp multiplier variable.
            sorted_timing_points[i].time_multiplier = multiplier * final_timing_points[-1].time_multiplier
            sorted_timing_points[i].update_beat_length()

            final_timing_points.append(sorted_timing_points[i])
            continue

        #checks if timing point is start/stop
        if i > 0 and sorted_timing_points[i].is_start_stop:
            time = sorted_timing_points[i].time

            # if time is same as previous timing points, updates previous timing points note generation flag
            if math.isclose(sorted_timing_points[i].time, final_timing_points[-1].time, abs_tol=0.001):
                final_timing_points[-1].is_start_stop = True
                final_timing_points[-1].generate_notes = not final_timing_points[-1].generate_notes

                #redundant I think
                final_timing_points[-1].update_beat_length()

                continue

            # copies properties of previous timing point
            sorted_timing_points[i] = copy.copy(final_timing_points[-1])

            # updates to current timing points properties
            sorted_timing_points[i].time = time
            sorted_timing_points[i].is_start_stop = True
            sorted_timing_points[i].is_bpm_change = False

            # flips note generation flag
            sorted_timing_points[i].generate_notes = not final_timing_points[-1].generate_notes

            # redundant I think
            sorted_timing_points[i].time_multiplier = final_timing_points[-1].time_multiplier
            sorted_timing_points[i].update_beat_length()

            final_timing_points.append(sorted_timing_points[i])

            continue

        # for all standard timing points other than the first, inherit previous timing points note generation flag and multiplier, then add to final timing points
        if i > 0:

            # only inherit properties if time is same
            if math.isclose(sorted_timing_points[i].time, final_timing_points[-1].time, abs_tol=0.001):
                is_start_stop = final_timing_points[-1].is_start_stop
                is_bpm_change = final_timing_points[-1].is_bpm_change

                final_timing_points[-1] = sorted_timing_points[i]
                final_timing_points[-1].is_start_stop = is_start_stop
                final_timing_points[-1].is_bpm_change = is_bpm_change
            else:
                sorted_timing_points[i].time_multiplier = final_timing_points[-1].time_multiplier
                sorted_timing_points[i].generate_notes = final_timing_points[-1].generate_notes
                sorted_timing_points[i].update_beat_length()
                final_timing_points.append(sorted_timing_points[i])

    return final_timing_points
