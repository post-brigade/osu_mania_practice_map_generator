import sys
from pathlib import Path

from src.functions import (
    add_chords,
    build_new_map,
    generate_note_matrix,
    generate_notes_with_timing_points,
    get_cli_arguments,
    get_difficulty_name,
    get_new_map_path,
    get_timing_changes,
    get_user_input,
    note_instructions_to_timing_changes,
    notes_to_note_instructions,
    read_map,
    write_map,
)


def main():
    should_print = True
    chord_tuples = None
    density_rating = 0

    if len(sys.argv) == 1:
        map_path, key_count, generation_type = get_user_input()

    else:
        map_path, key_count, generation_type, chord_tuples = get_cli_arguments(sys.argv)

    if chord_tuples:
        total_density = (
            chord_tuples[0][1]
            + chord_tuples[1][1]
            + 2 * chord_tuples[2][1]
            + 4 * chord_tuples[3][1]
            + 8 * chord_tuples[4][1]
        )
        density_rating = round(((total_density - 16 ) * (9 / 40)) + 1, 2)
        print(density_rating)

    difficulty_name = get_difficulty_name(generation_type, key_count, density_rating)

    new_map_path = get_new_map_path(difficulty_name, map_path)

    if new_map_path.exists():
        raise ValueError("File exists at output path")

    normal_lines, timing_points, notes = read_map(map_path, key_count, difficulty_name)

    sorted_notes = sorted(notes, key = lambda note: (note.time, note.column))

    note_instructions = notes_to_note_instructions(sorted_notes)

    timing_changes_from_map = get_timing_changes(timing_points)

    final_timing_changes = note_instructions_to_timing_changes(timing_changes_from_map, note_instructions)

    notes_to_map = generate_notes_with_timing_points(final_timing_changes, notes[-1], key_count)

    notes_to_map = add_chords(notes_to_map, generation_type, key_count, chord_tuples)

    generate_note_matrix(notes_to_map, final_timing_changes, should_print, key_count)

    new_map = build_new_map(normal_lines, final_timing_changes, notes_to_map)

    write_map(new_map, new_map_path)

if __name__ == "__main__":
    main()
