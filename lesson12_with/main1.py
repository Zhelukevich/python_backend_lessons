from pathlib import Path

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / "data.txt"

# with open(file_path, encoding="utf-8") as file:
#     content = file.read()
#     print(content)


class FileOpener:
    def __init__(self, file_path: str, mode: str) -> None:
        self.file_path = Path(file_path)
        if not self.file_path.is_absolute():
            self.file_path = BASE_DIR / self.file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc, tb) -> None:
        if self.file is not None:
            self.file.close()


with FileOpener("data.txt", "r") as file:
    print(file.read())
