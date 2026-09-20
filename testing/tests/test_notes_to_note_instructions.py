import unittest

from constants_for_testing import (
    KEY_COUNT,
    MAP_INPUT_DIR,
)
from src.classes import *
from src.functions import *


class Test(unittest.TestCase):

    def test_a_test_all_instruction_types(self):
        print("\nnotes_to_note_instructions tests")

        map_path = MAP_INPUT_DIR / "test_notes_to_note_instructions" / "test_a.osu"
        normal_lines, timing_points, notes = read_map(map_path, KEY_COUNT)
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
