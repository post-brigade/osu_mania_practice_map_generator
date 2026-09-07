from typing import override


class TimingPoint:
    def __init__(self,
        time: float,
        beat_length: float,
        meter: int,
        sample_set: int,
        sample_index: int,
        volume: int,
        uninherited: int,
        effects: int,
    ):
        self.timing_group: int | None = None
        self.is_generated: bool = False
        self.time_multiplier: float = 1

        self.time = time
        self.beat_length = beat_length
        self.meter = meter
        self.sample_set = sample_set
        self.sample_index = sample_index
        self.volume = volume
        self.uninherited = uninherited
        self.effects = effects
        self.bpm: float = 1 / beat_length * 1000 * 60

        self.active_beat_length = self.beat_length


    def update_beat_length(self):
        self.active_beat_length = self.beat_length * self.time_multiplier


    @override
    def __repr__(self):
        if self.uninherited == 1:
                return f"timing point: group: {self.timing_group} time:{round(self.time)} bpm: {round(self.bpm, 2)} meter: {self.meter} beat length: {round(self.active_beat_length)}"
        else:
            return f"timing point: time:{round(self.time)} meter: {self.meter}"


class Note:
    def __init__(self,
        x: int,
        y: int,
        time: float,
        type: int,
        hit_sound: int,
        hit_sample: str,
        key_count: int,
    ):
        self.x = x
        self.column: int = (x * key_count // 512) + 1
        self.y = y
        self.time = time
        self.type = type
        self.hit_sound = hit_sound
        self.hit_sample = hit_sample
        self.key_count = key_count

        self.timing_group: int | None = None
        self.delay:int | None = None

    @override
    def __repr__(self):
        return f"normal note: group: {self.timing_group} column:{self.column} time: {round(self.time)}"


class LongNote(Note):
    def __init__(self,
        x: int,
        y: int,
        time: float,
        type: int,
        hit_sound: int,
        end_time: float,
        hit_sample: str,
        key_count: int,
    ):
        super().__init__(x, y, time, type, hit_sound, hit_sample, key_count)
        self.end_time = end_time

    @override
    def __repr__(self):
        return f"long note: group: {self.timing_group} column:{self.column} time: {round(self.time)} end time: {round(self.end_time)}"
