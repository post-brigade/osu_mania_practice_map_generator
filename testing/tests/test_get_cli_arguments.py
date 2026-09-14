import unittest
from pathlib import Path

from src.classes import *
from src.functions import *

TESTING_HOME_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = TESTING_HOME_DIR  / "tests"
MAP_INPUT_DIR = TESTING_HOME_DIR  / "test_maps" / "read"
MAP_OUTPUT_DIR = TESTING_HOME_DIR  / "test_maps" / "write"
KEY_COUNT = 7

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

        x, y, z = get_cli_arguments(valid_args)

        # inactive for testing
        # with self.assertRaisesRegex(ValueError, "File exists at output path"):
        #     get_user_arguments(invalid_args)

        with self.assertRaisesRegex(ValueError, "Invalid input, need .osu file"):
            get_cli_arguments(invalid_args_2)

        with self.assertRaisesRegex(ValueError, "Invalid input, need .osu file"):
            get_cli_arguments(invalid_args_3)

        with self.assertRaisesRegex(ValueError, "Invalid density option: not 1, 2, 3, 4, or 5"):
            get_cli_arguments(invalid_args_5)


if __name__ == "__main__":
    unittest.main()
