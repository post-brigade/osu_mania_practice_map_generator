from src.classes import LongNote, Note, TimingPoint

from .to_lines import to_lines


def build_new_map(
    normal_lines: list[list[str]],
    timing_points: list[TimingPoint],
    notes: list[Note | LongNote],
    round_time:bool = False
) -> str:

    timing_point_lines = to_lines(timing_points, round_time)
    note_lines = to_lines(notes)
    new_lines: list[list[str]] = []

    for line in normal_lines:
        if line[0].lower() == "[TimingPoints]".lower():
            new_lines.append(line)
            for timing_point_line in timing_point_lines:
                new_lines.append(timing_point_line)

        elif line[0].lower() == "[HitObjects]".lower():
            new_lines.append(line)

            for note_line in note_lines:
                new_lines.append(note_line)

        else:
            new_lines.append(line)

    joined_lines : list[str] = []

    for line in new_lines:
        joined_lines.append(",".join(line))

    map = "\n".join(joined_lines)


    return map
