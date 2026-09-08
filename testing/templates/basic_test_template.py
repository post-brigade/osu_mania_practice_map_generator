import unittest
from pathlib import Path

from src.classes import *
from src.functions import *

TESTING_HOME_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = TESTING_HOME_DIR  / "tests"
MAP_INPUT_DIR = TESTING_HOME_DIR  / "maps" / "read"
MAP_OUTPUT_DIR= TESTING_HOME_DIR  / "maps" / "write"

class Test(unittest.TestCase):

    def test(self):
        pass



if __name__ == "__main__":
    unittest.main()
