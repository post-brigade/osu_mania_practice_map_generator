import unittest
from pathlib import Path

from src.classes import *
from src.functions import *

TESTING_HOME_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = TESTING_HOME_DIR  / "tests"
MAP_INPUT_DIR = TESTING_HOME_DIR  / "test_maps" / "read"
MAP_OUTPUT_DIR= TESTING_HOME_DIR  / "test_maps" / "write"
KEY_COUNT = 7

MAP_PATH = MAP_INPUT_DIR / "test_read_map" / "test_a.osu"

class Test(unittest.TestCase):

    def test_a_read_map_normal_lines(self):
        print("\nread_map tests")

        normal_lines, timing_points, notes = read_map(str(MAP_PATH), KEY_COUNT)
        result = normal_lines
        correct_result = [
            ['osu file format v128'],
            [''],
            ['[Difficulty]'],
            ['HPDrainRate: 7'],
            [''],
            ['[Events]'],
            ['// Background and Video events'],
            [''],
            ['[TimingPoints]'],
            [''],
            ['[HitObjects]']]

        self.assertListEqual(result, correct_result)


    def test_b_read_map_timing_points(self):
        normal_lines, timing_points, notes = read_map(str(MAP_PATH), KEY_COUNT)
        timing_point = timing_points[0]
        correct_timing_point = TimingPoint(
            2505,
            480,
            4,
            1,
            0,
            30,
            1,
            0
        )
        self.assertEqual(timing_point, correct_timing_point)


    def test_c_read_map_notes(self):
        map_path = MAP_INPUT_DIR / "hazy_test_read_map.osu"
        normal_lines, timing_points, notes = read_map(str(MAP_PATH), KEY_COUNT)
        note = notes[0]
        correct_note = Note(
            36,
            192,
            2505,
            1,
            0,
            "1:0:0:30:"
        )
        self.assertEqual(note, correct_note)


    def test_d_read_map_long_notes(self):
        map_path = MAP_INPUT_DIR / "hazy_test_read_map.osu"
        normal_lines, timing_points, notes = read_map(str(MAP_PATH), KEY_COUNT)
        long_note = notes[1]
        correct_long_note = LongNote(
            109,
            192,
            2625,
            128,
            0,
            2745,
            "1:0:0:30:"
        )
        self.assertEqual(long_note, correct_long_note)

#36,192,2505,128,0,2625,1:0:0:30:

if __name__ == "__main__":
    unittest.main()
