# Contact-Management-system
Author-Miraj Khan
<br>
A simple command-line Contact Management System built with Python. Contacts are stored in a JSON file so data persists between sessions.
## Features
- View all contacts
- Add a new contact (with duplicate name check)
- Search a contact by name
- Delete a contact by name
- Auto-save to JSON file after every change

## Project Structure

```
contact-management-system/
│
├── contact_management.py   # Main program
└── contacts.json           # Auto-generated on first run
```

## How to Run

**Requirements:** Python 3.12

```bash
python contact_management.py
```

> Note: `contacts.json` will be created automatically on the first run.

## Usage

```
....Contact Management System....
1. Show contacts
2. Add contact
3. Search contact
4. Delete contact
5. Exit
Enter Your choice(1-5):
```

## Concepts Used

- Python dictionaries and lists
- Functions
- JSON file handling (read/write)
- `for-else` pattern for search and duplicate detection
- `global` variable for shared state

## Author

**Md. Miraj Khan**  
First-year CSE Student, East West University  
GitHub: [@miraj-dev2](https://github.com/miraj-dev2)
