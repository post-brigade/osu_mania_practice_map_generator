import math
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
        self.is_bpm_change: bool = False
        self.time_multiplier: float = 1

        self.is_start_stop: bool = False
        self.generate_notes: bool = False

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
        self.bpm: float = 1 / self.active_beat_length * 1000 * 60


    def __eq__(self, other):
        if not isinstance(other, TimingPoint):
            return False

        return (
            self.is_bpm_change == other.is_bpm_change
            and math.isclose(self.time_multiplier, other.time_multiplier, abs_tol=0.001)
            and self.is_start_stop == other.is_start_stop
            and self.generate_notes == other.generate_notes
            and math.isclose(self.time, other.time, abs_tol=0.001)
            and math.isclose(self.beat_length, other.beat_length, abs_tol=0.001)
            and self.meter == other.meter
            and self.sample_set == other.sample_set
            and self.sample_index == other.sample_index
            and self.volume == other.volume
            and self.uninherited == other.uninherited
            and self.effects == other.effects
            and math.isclose(self.bpm, other.bpm, abs_tol=0.001)
            and math.isclose(self.active_beat_length, other.active_beat_length, abs_tol=0.001)
        )

    @override
    def __repr__(self):
        if self.uninherited == 1:
                return (
                    "timing point:\n"
                    f"\tbpm change: {self.is_bpm_change}\n"
                    f"\tstart/stop: {self.is_start_stop}\n"
                    f"\tgenerate_notes: {self.generate_notes}\n"
                    f"\ttime multiplier: {self.time_multiplier}\n"
                    f"\ttime: {self.time}\n"
                    f"\toriginal beat length: {self.beat_length}\n"
                    f"\tmeter: {self.meter}\n"
                    f"\tsample set: {self.sample_set}\n"
                    f"\tsample index: {self.sample_index}\n"
                    f"\tvolume: {self.volume}\n"
                    f"\tuninherited: {self.uninherited}\n"
                    f"\teffects {self.effects}\n"
                    f"\tbpm: {self.bpm}\n"
                    f"\tactive beat length: {self.active_beat_length}"
                )
        else:
            return f"timing point: time:{round(self.time)} meter: {self.meter}"
