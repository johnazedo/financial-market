from pathlib import Path

# Base directory of your project (adjust if needed)
BASE_DIR = Path(__file__).resolve().parent.parent

def get_file_path(filename: str) -> str:
    path = f'{BASE_DIR}/data/{filename}'
    return path