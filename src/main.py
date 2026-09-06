from src.functions import (
    add_chords,
    assign_timing_groups,
    build_new_map,
    generate_note_matrix,
    generate_notes_with_timing_points,
    get_timing_changes,
    read_map,
    write_map,
)


def main():
    key_count = 7
    map_path = "./maps/hazy_moon_night/hazy_test.osu"
    new_map_path = "./maps/hazy_moon_night/hazy_test_output.osu"

    normal_lines, timing_points, notes = read_map(map_path, key_count)
    timing_changes = get_timing_changes(timing_points)
    generated_notes = generate_notes_with_timing_points(timing_changes, notes, key_count)
    notes_with_chords = add_chords(generated_notes, key_count)

    assign_timing_groups(notes_with_chords, timing_changes)

    generate_note_matrix(notes_with_chords, timing_changes, key_count)

    new_map = build_new_map(normal_lines, timing_points, notes_with_chords)
    write_map(new_map, new_map_path)

if __name__ == "__main__":
    main()
