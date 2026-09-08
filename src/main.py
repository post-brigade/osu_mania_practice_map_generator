from src.functions import (
    add_chords,
    assign_timing_groups,
    build_new_map,
    column_to_x,
    generate_note_matrix,
    generate_notes_with_timing_points,
    get_timing_changes,
    note_instructions_to_timing_changes,
    notes_to_note_instructions,
    read_map,
    write_map,
)


def main():
    key_count = 7
    map_path = "/mnt/c/Users/postb/Desktop/hazy_moon_night/hazy_test.osu"
    new_map_path = "/mnt/c/Users/postb/Desktop/hazy_moon_night/hazy_test_output.osu"

    normal_lines, timing_points, notes = read_map(map_path, key_count)


    start_stops, bpm_changes = notes_to_note_instructions(notes)

    timing_changes_from_map = get_timing_changes(timing_points)

    timing_changes_with_instructions = note_instructions_to_timing_changes(timing_changes_from_map, start_stops + bpm_changes)  # works

    generated_notes = generate_notes_with_timing_points(timing_changes_with_instructions, notes, key_count)

    notes_with_chords = add_chords(generated_notes, key_count)


    assign_timing_groups(notes_with_chords, timing_changes_with_instructions)

    generate_note_matrix(notes_with_chords, timing_changes_with_instructions, key_count)

    new_map = build_new_map(normal_lines, timing_changes_with_instructions, notes_with_chords)
    write_map(new_map, new_map_path)

if __name__ == "__main__":
    main()
