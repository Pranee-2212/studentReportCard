# Student Report Card (CLI)

A simple Python command-line app to manage student marks, calculate averages, assign grades, and persist data to `data.json`.

### Features
- Add, update, delete students
- View a report of all students (marks, average, grade)
- Persistent storage in `data.json`

### Project Structure
- `app.py`: CLI menu and program entry
- `classes.py`: `Student` and `GradeManager` classes
- `jsonFile_handler.py`: Save/load helpers for `data.json`
- `data.json`: JSON data store for students

### Requirements
- Python 3.8+

### Setup
1. Clone or download the project.
2. (Optional) Create a virtual environment.
3. Ensure `data.json` exists with valid JSON (a prefilled dataset is included).

### Running the App
```bash
python app.py
```

### Using the CLI
You will see a menu with options:
1. Display Report: prints each student's marks, average, and grade.
2. Add new Student: prompts for name and three marks (Math, English, Science). An ID like `123-A` is auto-generated.
3. Update student Records: provides student ID, then enter `subject,score` to add/update that subject.
4. Delete a student Record: removes a student by ID.
5. Exit: saves current data back to `data.json`.

Notes:
- Subjects are stored as a dictionary; new subjects can be added during update.
- Grades are computed from average: A (>=90), B (>=80), C (>=70), F (<70).

### Data Format (data.json)
`data.json` is an object whose keys are numeric strings ("0", "1", ...). Each value is a student record:
```json
{
  "0": {
    "id": "101-A",
    "name": "Alice Johnson",
    "subjects": {"Math": 95, "English": 88, "Science": 92},
    "grade": "A",
    "average": 91.67
  }
}
```

### Common Issues
- If `data.json` is empty/invalid, the app may fail to load. Ensure it contains valid JSON.
- When adding via CLI, enter marks as comma-separated integers, e.g.: `90,80,85`.

### Extend the App
- Add more subjects or validation for scores.
- Improve CLI input handling and error messages.
- Build a GUI or web API on top of `GradeManager`.

### License
MIT


