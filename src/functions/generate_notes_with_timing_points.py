import math

from src.classes import LongNote, Note, TimingPoint

from .generate_note import generate_note


def generate_notes_with_timing_points(timing_changes: list[TimingPoint], final_note: Note, key_count: int):
    time_tick = timing_changes[0].active_beat_length / 4

    new_notes: list[Note] = []
    banned_columns = set()

    for i in range(len(timing_changes)):
        current_time = timing_changes[i].time
        time_tick = timing_changes[i].active_beat_length / 4
        generate_notes = timing_changes[i].generate_notes

        while(
            (current_time > timing_changes[i].time or math.isclose(current_time, timing_changes[i].time, abs_tol=0.001))
            and current_time < (timing_changes[i + 1].time - .001)

            if i < len(timing_changes) - 1 else

            (current_time > timing_changes[i].time or math.isclose(current_time, timing_changes[i].time, abs_tol=0.001))
            and (current_time < final_note.time or math.isclose(current_time, final_note.time, abs_tol=0.001))
        ):
            if generate_notes:
                note = generate_note(current_time, 1, key_count, banned_columns)
                banned_columns = {note.column}
                new_notes.append(note)

            current_time += time_tick

    return new_notes
