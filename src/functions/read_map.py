import re

from src.classes import LongNote, Note, TimingPoint

from .create_long_note import create_long_note
from .create_note import create_note
from .create_timing_point import create_timing_point


def read_map(map_path: str, key_count: int) -> tuple[list[list[str]], list[TimingPoint], list[Note | LongNote]]:
    normal_note_pattern = re.compile(r"\d+,\d+,\d+(?:\.\d+)?,1,\d,\d:\d:\d:\d{1,3}:")
    long_note_pattern = re.compile(r"\d+,\d+,\d+(?:\.\d+)?,128,\d,\d+(?:\.\d+)?,\d:\d:\d:\d{1,3}:")
    timing_point_pattern = re.compile(r"\d+,-?\d+(?:\.\d+)?,\d{1},\d{1},\d,\d{1,3},\d,\d{1,2}")

    timing_points: list[TimingPoint] = []
    notes: list[Note | LongNote] = []
    normal_lines: list[list[str]] = []

    with open(map_path) as map:

        for line in map:
            line_stripped = line.strip()
            line_split = line_stripped.split(",")

            if line == "":
                normal_lines.append([line])
                continue
            match_t = timing_point_pattern.search(line)
            match_n = normal_note_pattern.search(line)
            match_ln = long_note_pattern.search(line)

            if match_n:
                note = create_note(line_split, key_count)
                notes.append(note)

            elif match_ln:
                long_note = create_long_note(line_split, key_count)
                notes.append(long_note)

            elif match_t:
                timing_point = create_timing_point(line_split)
                timing_points.append(timing_point)

            else:
                normal_lines.append(line_split)

        return normal_lines, timing_points, notes
