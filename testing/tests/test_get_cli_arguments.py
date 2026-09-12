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
        print("\nget_user_arguments tests")
        no_input = str(MAP_INPUT_DIR / "test_get_user_arguments" / "fake.osu")
        incorrect_input = str(MAP_INPUT_DIR / "test_get_user_arguments" / "test_a.txt")
        existing_output = str(MAP_OUTPUT_DIR / "test_get_user_arguments" /"exists.osu")
        no_output_folder = str(MAP_OUTPUT_DIR / "fake_folder" /"exists.osu")

        valid_input = str(MAP_INPUT_DIR / "test_get_user_arguments" / "test_a.osu")
        valid_output = str(MAP_OUTPUT_DIR / "test_get_user_arguments" /"test_a_output.osu")

        valid_args = [
            " ",
            valid_input,
            valid_output,
            "4",
            "1"
        ]
        invalid_args = [
            " ",
            valid_input,
            existing_output,
            "4",
            "1"
        ]
        invalid_args_2 = [
            " ",
            no_input,
            valid_output,
            "7",
            "2"
        ]
        invalid_args_3 = [
            " ",
            incorrect_input,
            valid_output,
            "7",
            "3"
        ]
        invalid_args_4 = [
            " ",
            valid_input,
            no_output_folder,
            "7",
            "1"
        ]
        invalid_args_5 = [
            " ",
            valid_input,
            valid_output,
            "7",
            "6"
        ]

        w, x, y, z = get_cli_arguments(valid_args)

        # inactive for testing
        # with self.assertRaisesRegex(ValueError, "File exists at output path"):
        #     get_user_arguments(invalid_args)

        with self.assertRaisesRegex(ValueError, "Invalid input, need .osu file"):
            get_cli_arguments(invalid_args_2)

        with self.assertRaisesRegex(ValueError, "Invalid input, need .osu file"):
            get_cli_arguments(invalid_args_3)

        with self.assertRaisesRegex(ValueError, "Output directory does not exist"):
            get_cli_arguments(invalid_args_4)

        with self.assertRaisesRegex(ValueError, "Invalid generation type: 1: stream, 2: light chordstream, 3: dense chordstream"):
            get_cli_arguments(invalid_args_5)




if __name__ == "__main__":
    unittest.main()
