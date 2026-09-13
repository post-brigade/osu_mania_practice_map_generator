from pathlib import Path


def get_new_map_path(difficulty_name: str, map_path: Path):
    new_file_name = difficulty_name + " " + map_path.name
    new_map_path = map_path.with_name(new_file_name)

    return new_map_path
