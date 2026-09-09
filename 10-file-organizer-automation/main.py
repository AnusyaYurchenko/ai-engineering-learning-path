from pathlib import Path

FILE_CATEGORIES = {
    "documents": [".pdf", ".rtf", ".txt", ".docx"],
    "spreadsheets": [".csv", ".xlsx"],
    "images": [".jpg", ".jpeg", ".png"],
    "audio": [".m4a", ".m4b", ".mp3"],
    "videos": [".mov", ".avi", ".mp4"]
}

SKIP_FILES = {"main.py", "README.md", "requirements.txt", ".gitignore"}


def choose_folder(file_extension):
    for folder_name, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return folder_name

    return "misc"


def create_unique_path(destination_path):
    if not destination_path.exists():
        return destination_path

    counter = 1
    file_stem = destination_path.stem
    file_extension = destination_path.suffix
    folder = destination_path.parent

    while True:
        new_path = folder / f"{file_stem}_{counter}{file_extension}"

        if not new_path.exists():
            return new_path

        counter += 1


def organize_folder(folder_path):
    folder = Path(folder_path)
    moved_files = []

    for item in folder.iterdir():
        if item.is_dir() or item.name in SKIP_FILES:
            continue

        file_extension = item.suffix.lower()
        destination_folder_name = choose_folder(file_extension)
        destination_folder = folder / destination_folder_name
        destination_folder.mkdir(exist_ok=True)

        destination_path = create_unique_path(destination_folder / item.name)
        item.rename(destination_path)

        moved_files.append({
            "file": item.name,
            "moved_to": str(destination_path)
        })

    return moved_files


def print_report(moved_files):
    if not moved_files:
        print("No files were moved.")
        return

    print("Files organized:")

    for item in moved_files:
        print(f"- {item['file']} -> {item['moved_to']}")


def main():
    current_folder = Path.cwd()
    moved_files = organize_folder(current_folder)
    print_report(moved_files)


if __name__ == "__main__":
    main()
