from src.classes import LongNote, Note, TimingPoint


def assign_timing_groups(
    notes: list[Note | LongNote],
    timing_changes: list[TimingPoint]
) -> list[list[Note | LongNote]]:
    if not timing_changes:
        return []

    timing_groups: list[list[Note | LongNote]] = [
        [] for _ in timing_changes
    ]
    note_index = 0

    while (
        note_index < len(notes)
        and notes[note_index].time < timing_changes[0].time
    ):
        note_index += 1

    for i in range(len(timing_changes)):
        timing_changes[i].timing_group = i
        if i < len(timing_changes) - 1:
            for note in notes[note_index:]:
                if note.time >= timing_changes[i + 1].time:
                    break
                if note.time >= timing_changes[i].time:
                    note.timing_group = i
                    timing_groups[i].append(note)
                    note_index += 1
                    continue

    for note in notes[note_index:]:
        note.timing_group = len(timing_changes)-1
        timing_groups[-1].append(note)

    return timing_groups
