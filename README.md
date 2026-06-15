#  GPA-Maxxing-Tracker

A Python tool that tracks module grades and calculates a
weighted CGPA based on the Singapore Polytechnic grading system.

This project was developed over the course of one week as a personal exercise to apply Python fundamentals, particularly in file handling, data structures, and algorithmic problem solving, to a practical real-world inspired use case.

# Features

- Add modules with name, Credit Units (CU), and percentage scored 
- Automatically converts percentage into SP grade letters and grade points e.g.(4.0, 3.5, etc.)
- Calculates weighted CGPA (accounts for Credit Units)
- Editing of a module's mark
- Data is saved to grades.csv so it persists between runs

# How it works

On startup the program reads grades.csv (if it exists) into a list of
dictionaries, one per module. Adding or editing a module updates that list
and rewrites the file. Grade conversion follows SP's official mark-to-grade
point table:


| Mark Range | Grade | Grade Point |
| --- | --- | --- |
| 80–100 | A | 4.0|
| 75 - 79 | B+ | 3.5 |
| 70 - 74 | B | 3.0 |
| 65 - 69 | C+ | 2.5 |
| 60 - 64 | C | 2.0 |
| 55 - 59 | D+ | 1.5 |
| 50 - 54 | D | 1.0 |
| 45 - 49 | D- | 0.5 |
| < 45 | F | 0.0 |

# Running it

The program should be placed in a single folder:

GPA-Tracker/
 ├── main.py
 ├── grades.csv (auto-created after first run)
 └── README.md

grades.csv is automatically created in the same directory as main.py when the program is first run. It stores all module data and allows the information to persist between sessions.


# Built with

Python (standard library only: csv, os)

# Possible future additions

- Graph of CGPA trend across semesters( need to learn matplotlib)
- module deletion feature
