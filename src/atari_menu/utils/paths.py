from pathlib import Path
def relative_root_project(path: str):
    return str(Path(__file__).parents[3] / path)
