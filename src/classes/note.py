from typing import override


class Note:
    def __init__(self,
        x: int,
        y: int,
        time: float,
        type: int,
        hit_sound: int,
        hit_sample: str,
        key_count: int = 7,
    ):
        self.x = x
        self.column: int = (x * key_count // 512) + 1
        self.y = y
        self.time = time
        self.type = type
        self.hit_sound = hit_sound
        self.hit_sample = hit_sample
        self.key_count = key_count


    def __eq__(self, other):
        if not isinstance(other, Note):
            return False

        return (
            self.x == other.x
            and self.column == other.column
            and self.y == other.y
            and self.time == other.time
            and self.type == other.type
            and self.hit_sound  == other.hit_sound
            and self.hit_sample == other.hit_sample
            and self.key_count == other.key_count
        )

    @override
    def __repr__(self):
        return f"normal note: x: {self.x} column:{self.column} time: {round(self.time)}"
