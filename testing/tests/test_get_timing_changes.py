import unittest
from pathlib import Path

from src.classes import *
from src.functions import *

TESTING_HOME_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = TESTING_HOME_DIR  / "tests"
MAP_INPUT_DIR = TESTING_HOME_DIR  / "test_maps" / "read"
MAP_OUTPUT_DIR= TESTING_HOME_DIR  / "test_maps" / "write"
KEY_COUNT = 7

class Test(unittest.TestCase):

    def test_a_test_all_instruction_types(self):
        print("\nget_timing_changes tests")

        map_path = MAP_INPUT_DIR / "test_get_timing_changes" / "test_a.osu"
        normal_lines, timing_points, notes = read_map(str(map_path), KEY_COUNT)
        timing_changes = get_timing_changes(timing_points)

        correct_change_1 = TimingPoint(2505, 480, 4, 1, 0, 30, 1, 0)
        correct_change_2 = TimingPoint(64425, 480, 4, 1, 0, 30, 1, 1)
        correct_change_3 = TimingPoint(154185, 480, 4, 1, 0, 30, 1, 0)

        self.assertEqual(len(timing_changes), 3)

        self.assertEqual(timing_changes[0], correct_change_1)
        self.assertEqual(timing_changes[1], correct_change_2)
        self.assertEqual(timing_changes[2], correct_change_3)


if __name__ == "__main__":
    unittest.main()
