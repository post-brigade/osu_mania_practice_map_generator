from src.classes import LongNote, Note, TimingPoint

from .generate_note import generate_note


def generate_notes_with_timing_points(timing_changes: list[TimingPoint], notes: list[Note], key_count: int):

    # starts at a 16th note
    time_tick = timing_changes[0].beat_length / 4

    new_notes: list[Note] = []
    banned_columns = set()
    generate_notes = False

    #pulls instruction and timestamp from note: (instruction, time stamp)
    input_from_notes: list[tuple] = []

    for note in notes:
        input_from_notes.append((note.column, note.time))

    for i in range(len(timing_changes)):
        current_time = timing_changes[i].time

        while(
            current_time >= timing_changes[i].time
            and current_time < timing_changes[i + 1].time

            if i < len(timing_changes) - 1 else

            current_time >= timing_changes[i].time
            and current_time <= notes[-1].time
        ):
            for j in range(len(input_from_notes)):
                if current_time <= input_from_notes[j][1] < current_time + time_tick:

                    match input_from_notes[j][0]:
                        case 1:
                            generate_notes = True
                        case 2:
                            generate_notes = False
                        case 3:
                            time_tick /= 2
                        case 3:
                            time_tick *= 2
                        case _:
                            pass

                if generate_notes == True:
                    note = generate_note(current_time, 1, key_count, banned_columns)
                    banned_columns = {note.column}
                    new_notes.append(note)
                current_time += time_tick

    return new_notes
