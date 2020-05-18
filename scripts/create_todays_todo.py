from pathlib import Path
from datetime import date

if __name__ == "__main__":

    parent_path = Path(Path.home() / 'daily_todos').mkdir(parents=True, exist_ok=True)
