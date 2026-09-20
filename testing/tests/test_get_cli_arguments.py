import unittest

from constants_for_testing import (
    MAP_INPUT_DIR,
)
from src.classes import *
from src.functions import *

MAP_PATH = MAP_INPUT_DIR / "test_get_user_arguments" / "test_a.osu"

class Test(unittest.TestCase):

    def test_a_get_paths(self):
        print("\nget_cli_arguments tests")
        no_input = str(MAP_INPUT_DIR / "test_get_cli_arguments" / "fake.osu")
        incorrect_input = str(MAP_INPUT_DIR / "test_get_cli_arguments" / "test_a.txt")

        valid_input = str(MAP_INPUT_DIR / "test_get_cli_arguments" / "test_a.osu")

        valid_args = [
            " ",
            "4",
            "1",
            valid_input,
        ]
        invalid_args_2 = [
            " ",
            "7",
            "2",
            no_input
        ]
        invalid_args_3 = [
            " ",
            "7",
            "3",
            incorrect_input
        ]
        invalid_args_5 = [
            " ",
            "7",
            "6",
            valid_input,
        ]

        w, x, y, z = get_cli_arguments(valid_args)

        with self.assertRaisesRegex(ValueError, "Invalid input, need .osu file"):
            get_cli_arguments(invalid_args_2)

        with self.assertRaisesRegex(ValueError, "Invalid input, need .osu file"):
            get_cli_arguments(invalid_args_3)

        with self.assertRaisesRegex(ValueError, "Invalid density option: should be 1 to 5, 0 for custom"):
            get_cli_arguments(invalid_args_5)


if __name__ == "__main__":
    unittest.main()
