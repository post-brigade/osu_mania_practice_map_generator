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
        print("\nnotes_to_note_instructions tests")

        map_path = MAP_INPUT_DIR / "test_notes_to_note_instructions" / "test_a.osu"
        normal_lines, timing_points, notes = read_map(str(map_path), KEY_COUNT)
        instructions = notes_to_note_instructions(notes)

        correct_instructions = [
            (1, 2505),
            (3, 3105),
            (2, 3705),
            (1, 4305),
            (4, 4905)
        ]

        self.assertEqual(instructions, correct_instructions)




if __name__ == "__main__":
    unittest.main()
