# moodle-automation

Contains various scripts for automation of tedious tasks. They can be used for some Moodle installations at Sofia University "St. Kliment Ohridski" but they can also be fully customized.

`remote-exam-sessions.py`: Creates separate BigBlueButton session for each student.

## Installation

- Install geckodriver (for Firefox).
- `pip3 install -r requirements.txt`

## Configuration

- Open the `.py` file and modify the parameters section (this will be improved in some future version).
- Create any input files needed (for example, `remote-exam-sessions.py` requires `remote-exam-students.csv`).

## Running

- Execute the `.py` file with Python 3.
- Moodle credentials should be entered within 12 seconds after showing the sign-in page.

