import unittest
from pathlib import Path

from src.classes import *
from src.functions import *

TESTING_HOME_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = TESTING_HOME_DIR  / "tests"
MAP_INPUT_DIR = TESTING_HOME_DIR  / "maps" / "read"
MAP_OUTPUT_DIR= TESTING_HOME_DIR  / "maps" / "write"
KEY_COUNT = 7

class Test(unittest.TestCase):

    def test_a_normal_function(self):
        print("\nnote_instructions_to_timing_changes tests")

        map_path = MAP_INPUT_DIR / "test_note_instructions_to_timing_changes" / "test_a.osu"
        normal_lines, timing_points, notes = read_map(str(map_path), KEY_COUNT)
        instructions = notes_to_note_instructions(notes)
        timing_changes_from_map = get_timing_changes(timing_points)
        final_timing_changes = note_instructions_to_timing_changes(timing_changes_from_map, instructions)

        timing_change_1 = TimingPoint(2505, 480, 4, 1, 0, 30, 1, 0)
        timing_change_1.is_start_stop = True
        timing_change_1.generate_notes = True

        timing_change_2 = TimingPoint(3105, 480, 4, 1, 0, 30, 1, 1)
        timing_change_2.generate_notes = timing_change_1.generate_notes
        timing_change_2.is_bpm_change = True
        timing_change_2.time_multiplier = .5
        timing_change_2.update_beat_length()

        timing_change_3 = TimingPoint(3705, 480, 4, 1, 0, 30, 1, 1)
        timing_change_3.is_start_stop = True
        timing_change_3.generate_notes = False
        timing_change_3.time_multiplier = timing_change_2.time_multiplier
        timing_change_3.update_beat_length()

        timing_change_4 = TimingPoint(4065, 480, 4, 1, 0, 30, 1, 0)
        timing_change_4.generate_notes = timing_change_3.generate_notes
        timing_change_4.time_multiplier = timing_change_3.time_multiplier
        timing_change_4.update_beat_length()

        timing_change_5 = TimingPoint(4305, 480, 4, 1, 0, 30, 1, 0)
        timing_change_5.is_start_stop = True
        timing_change_5.generate_notes = True
        timing_change_5.time_multiplier = timing_change_4.time_multiplier
        timing_change_5.update_beat_length()

        timing_change_6 = TimingPoint(4905, 480, 4, 1, 0, 30, 1,0)
        timing_change_6.is_bpm_change = True
        timing_change_6.time_multiplier = 1
        timing_change_6.generate_notes = timing_change_5.generate_notes
        timing_change_6.update_beat_length()

        timing_change_7 = TimingPoint(5265, 480, 4, 1, 0, 30, 1, 1)
        timing_change_7.generate_notes = timing_change_6.generate_notes
        timing_change_7.time_multiplier = timing_change_6.time_multiplier
        timing_change_7.update_beat_length()

        self.assertEqual(len(final_timing_changes), 7)
        self.assertEqual(final_timing_changes[0], timing_change_1)
        self.assertEqual(final_timing_changes[1], timing_change_2)
        self.assertEqual(final_timing_changes[2], timing_change_3)
        self.assertEqual(final_timing_changes[3], timing_change_4)
        self.assertEqual(final_timing_changes[4], timing_change_5)
        self.assertEqual(final_timing_changes[5], timing_change_6)
        self.assertEqual(final_timing_changes[6], timing_change_7)


if __name__ == "__main__":
    unittest.main()
