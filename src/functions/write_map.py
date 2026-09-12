from pathlib import Path


def write_map(map: str, map_path: Path):
     with open(map_path, "w") as file: # "w" for debugging, will be "x"
         file.write(map)
