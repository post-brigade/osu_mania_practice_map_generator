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


def check_note_timings(notes: list[Note], last_note: Note) -> bool:
    if not notes:
        return False

    for note in notes:
        if ((note.time > 3705 or math.isclose(note.time, 3705, abs_tol=0.001))
            and note.time < 4305 - .001):
            return False

        if note.time > last_note.time + .001:
            return False

    return True


def check_bpm(notes: list[Note]):
    if not notes:
        return False

    for i in range(len(notes)):
        if  math.isclose(notes[i].time, 3105, abs_tol=0.001) and not math.isclose(notes[i + 1].time - notes[i].time, 240 / 4, abs_tol=0.001):
            return False

        if  math.isclose(notes[i].time, 4905, abs_tol=0.001) and not math.isclose(notes[i + 1].time - notes[i].time, 480 / 4, abs_tol=0.001):
            return False

    return True


class Test(unittest.TestCase):

    def test_a_normal_function(self):
        print("\ngenerate_notes_with_timing_points tests")

        map_path = MAP_INPUT_DIR / "test_generate_notes_with_timing_points" / "test_a.osu"
        normal_lines, timing_points, notes = read_map(str(map_path), KEY_COUNT)
        instructions = notes_to_note_instructions(notes)
        timing_changes_from_map = get_timing_changes(timing_points)
        final_timing_changes = note_instructions_to_timing_changes(timing_changes_from_map, instructions)

        generated_notes = generate_notes_with_timing_points(final_timing_changes, notes[-1], KEY_COUNT)

        generating_correct = check_note_timings(generated_notes, notes[-1])
        bpm_correct = check_bpm(generated_notes)

        self.assertTrue(generating_correct and bpm_correct)

# [TimingPoints]
# 2505,480,4,1,0,30,1,0
# 3105,480,4,1,0,30,1,1
# 4065,480,4,1,0,30,1,0
# 5265,480,4,1,0,30,1,1


# [HitObjects]
# 36,192,2505,1,0,1:0:0:30:
# 182,192,3105,25,1,0,1:0:0:30:
# 109,192,3705,1,0,1:0:0:30:
# 36,192,4305,1,0,1:0:0:30:
# 256,192,4905,1,0,1:0:0:30:
# 475,192,6225,1,0,1:0:0:30:

if __name__ == "__main__":
    unittest.main()
