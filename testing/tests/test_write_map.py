import os
import unittest
from pathlib import Path

from src.classes import *
from src.functions import *

TESTING_HOME_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = TESTING_HOME_DIR  / "tests"
MAP_INPUT_DIR = TESTING_HOME_DIR  / "test_maps" / "read"
MAP_OUTPUT_DIR= TESTING_HOME_DIR  / "test_maps" / "write"
KEY_COUNT = 7

def simple_read_map(map_path):
    map_lines: list[str] = []

    with open(map_path) as file:
        for line in file:
            line_stripped = line.strip()
            map_lines.append(line_stripped)

    map = "\n".join(map_lines)
    return map


class Test(unittest.TestCase):
    def test_a_check_first_chords(self):
        print("\nwrite_map tests")

        map_path = MAP_INPUT_DIR / "test_write_map" / "test_a.osu"
        new_map_path = MAP_OUTPUT_DIR / "test_write_map" / "test_a.osu"
        normal_lines, timing_points, notes = read_map(map_path, KEY_COUNT)

        comparison_map = simple_read_map(map_path)
        new_map = build_new_map(normal_lines, timing_points, notes, True)

        write_map(new_map, new_map_path)

        with open(new_map_path) as file:
            new_map_read = file.read()

        self.maxDiff = None
        self.assertEqual(comparison_map, new_map_read)

        os.remove(new_map_path)



if __name__ == "__main__":
    unittest.main()
