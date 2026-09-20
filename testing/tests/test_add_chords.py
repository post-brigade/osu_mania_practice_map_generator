import math
import unittest
from pathlib import Path

from src.classes import *
from src.functions import *

TESTING_HOME_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = TESTING_HOME_DIR  / "tests"
MAP_INPUT_DIR = TESTING_HOME_DIR  / "test_maps" / "read"
MAP_OUTPUT_DIR= TESTING_HOME_DIR  / "test_maps" / "write"
KEY_COUNT = 7

def chord_is_valid(chord: list[Note]) -> bool:
    chord_times = [note.time for note in chord]
    chord_columns = [note.column for note in chord]
    chord_correct = (
        math.isclose(max(chord_times), min(chord_times), abs_tol = .001)
        and len(chord_columns) == len(set(chord_columns))
    )
    return chord_correct


class Test(unittest.TestCase):

    def test_a_check_dense_chords(self):
        print("\nadd_chords tests")
        generation_type = 5
        map_path = MAP_INPUT_DIR / "test_add_chords" / "test_a.osu"
        normal_lines, timing_points, notes = read_map(map_path, KEY_COUNT)
        instructions = notes_to_note_instructions(notes)
        timing_changes_from_map = get_timing_changes(timing_points)
        final_timing_changes = note_instructions_to_timing_changes(timing_changes_from_map, instructions)
        generated_notes = generate_notes_with_timing_points(final_timing_changes, notes[-1], KEY_COUNT)
        notes_with_chords = add_chords(generated_notes, generation_type, KEY_COUNT)

        self.assertTrue(chord_is_valid(notes_with_chords[0:4]))
        self.assertTrue(chord_is_valid(notes_with_chords[5:7]))
        self.assertTrue(chord_is_valid(notes_with_chords[8:11]))
        self.assertTrue(chord_is_valid(notes_with_chords[12:14]))
        self.assertTrue(chord_is_valid(notes_with_chords[15:19]))

if __name__ == "__main__":
    unittest.main()
