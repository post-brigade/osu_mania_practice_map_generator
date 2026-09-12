import math
import re
import unittest
from pathlib import Path

from src.classes import *
from src.functions import *

TESTING_HOME_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = TESTING_HOME_DIR  / "tests"
MAP_INPUT_DIR = TESTING_HOME_DIR  / "test_maps" / "read"
MAP_OUTPUT_DIR= TESTING_HOME_DIR  / "test_maps" / "write"
KEY_COUNT = 7

def strip_formatting(string:str):
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    clean_string = ansi_escape.sub("", string)

    return clean_string


def check_first_character(line: list[str], char:str, is_barline: bool) -> bool:

    line_str = "".join(line)
    clean_line = strip_formatting(line_str)
    first_char = clean_line[0]

    return first_char == char


def check_notes(line: list[str], notes:list[Note]) -> bool:
    notes_correct: list[bool] = []

    for note in notes:
        bare_note = strip_formatting(line[note.column - 1])
        notes_correct.append(bare_note[1:4] == "▆▆▆")

    return all(notes_correct)


def check_note_matrix(note_matrix: list[list[str]], notes: list[Note]) -> bool | None:
    if not note_matrix:
        return None

    first_barline = check_first_character(note_matrix[0], "▁", True)
    second_barline = check_first_character(note_matrix[8], "▁", True)
    non_barlines = all(check_first_character(line, " ", False) for line in note_matrix[1:8])

    barlines_correct = all([first_barline, second_barline, non_barlines])

    line_1 = check_notes(note_matrix[0], notes[0:4])
    line_2 = check_notes(note_matrix[1], [notes[4]])
    line_3 = check_notes(note_matrix[2], notes[5:7])
    line_4 = check_notes(note_matrix[3], [notes[7]])
    line_5 = check_notes(note_matrix[4], notes[8:11])

    note_placement_correct = all([line_1, line_2, line_3, line_4, line_5])

    return barlines_correct and note_placement_correct


class Test(unittest.TestCase):
    def test_a_check_first_chords(self):
        print("\ngenerate_note_matrix tests")
        generation_type = 3
        map_path = MAP_INPUT_DIR / "test_generate_note_matrix" / "test_a.osu"
        normal_lines, timing_points, notes = read_map(map_path, KEY_COUNT)
        instructions = notes_to_note_instructions(notes)
        timing_changes_from_map = get_timing_changes(timing_points)
        final_timing_changes = note_instructions_to_timing_changes(timing_changes_from_map, instructions)
        generated_notes = generate_notes_with_timing_points(final_timing_changes, notes[-1], KEY_COUNT)
        notes_with_chords = add_chords(generated_notes, generation_type, KEY_COUNT)
        note_matrix = generate_note_matrix(notes_with_chords, final_timing_changes, False, KEY_COUNT)

        if note_matrix:
            note_matrix_correct = check_note_matrix(note_matrix, notes_with_chords)
        else:
            note_matrix_correct = False

        self.assertTrue(note_matrix_correct)

if __name__ == "__main__":
    unittest.main()
