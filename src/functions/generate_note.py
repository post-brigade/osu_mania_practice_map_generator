from src.classes import LongNote, Note, TimingPoint

from .column_and_bpm_helpers import column_to_x, random_column
from .create_long_note import create_long_note
from .create_note import create_note


def generate_note(time:float, type:int, key_count:int, banned_columns: set[int]) -> Note:
    column = random_column(banned_columns, key_count)
    x = column_to_x(column, key_count)
    props = [
        x,
        192,
        time,
        type,
        0,
        "0:0:0:30",
    ]
    note = create_note(props, key_count)

    return note
