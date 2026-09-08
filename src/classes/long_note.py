from typing import override

from .note import Note


class LongNote(Note):
    def __init__(self,
        x: int,
        y: int,
        time: float,
        type: int,
        hit_sound: int,
        end_time: float,
        hit_sample: str,
        key_count: int = 7,
    ):
        super().__init__(x, y, time, type, hit_sound, hit_sample, key_count)
        self.end_time = end_time


    def __eq__(self, other):
        if not isinstance(other, LongNote):
            return False

        return (
            self.x == other.x
            and self.column == other.column
            and self.y == other.y
            and self.time == other.time
            and self.type == other.type
            and self.hit_sound  == other.hit_sound
            and self.end_time == other.end_time
            and self.hit_sample == other.hit_sample
            and self.key_count == other.key_count
        )

    @override
    def __repr__(self):
        return f"long note: column:{self.column} time: {round(self.time)} end time: {round(self.end_time)}"
