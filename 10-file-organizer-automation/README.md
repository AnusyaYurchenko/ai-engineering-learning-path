# File Organizer Automation

## Problem

Business folders can become messy when invoices, reports, images, audio files, and other files are saved in one place.

This project organizes files automatically by moving them into folders based on their file type.

## How It Works

The script checks every file in the current folder.

For each file, it:

1. Checks the file extension.
2. Chooses the correct destination folder.
3. Creates the folder if it does not exist.
4. Moves the file into the correct folder.
5. Prints a short report of what was moved.

The script skips project files like `main.py`, `README.md`, `requirements.txt`, and `.gitignore`.

## Project Structure

```text
10-file-organizer-automation/
├── README.md
├── main.py
├── requirements.txt
├── .gitignore
├── sample_invoice.txt
├── sample_customers.csv
└── sample_notes.md
```

After running the script, files can be moved into folders like:

```text
documents/
spreadsheets/
images/
audio/
videos/
misc/
```

## Setup

This project uses only Python standard libraries, so there are no external packages to install.

## How To Run

Run the script from inside the project folder:

```powershell
python main.py
```

## Example Output

```text
Files organized:
- sample_invoice.txt -> C:\path\to\project\documents\sample_invoice.txt
- sample_customers.csv -> C:\path\to\project\spreadsheets\sample_customers.csv
- sample_notes.md -> C:\path\to\project\misc\sample_notes.md
```

## What I Learned

In this project, I practiced:

- working with folders and file paths
- using `pathlib.Path`
- checking file extensions
- creating folders with `.mkdir()`
- moving files with `.rename()`
- using dictionaries for file category rules
- avoiding duplicate file names
- writing cleaner automation scripts with functions

## Business Value

This kind of script can save time for people who regularly download or receive many business files. It can help keep reports, invoices, spreadsheets, images, and other files organized automatically.
