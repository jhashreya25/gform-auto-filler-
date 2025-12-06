Google Form Automation — Python + Selenium

A configurable, scalable Google Form automation tool built using Python and Selenium.
The system reads user data from a dataset (CSV) and automatically fills and submits Google Forms with human-like behaviour, dynamic field mapping, and detailed reporting.

This project demonstrates strong skills in automation, growth experimentation, analytics, and clean engineering design.

 Key Features
 1. Automated Google Form Submission

Automatically fills and submits any Google Form.

Supports multiple form structures.

 2. Dynamic Field Mapping (Config-Based)

Field names are mapped using a JSON config.

No need to modify code when switching forms.

 3. Dataset Input

Reads data from:

CSV (default)

Easily extendable to Excel/JSON

 4. Human-Like Behaviour Simulation

Random typing speed

Dynamic delays between interactions

Improves reliability and reduces detection

 5. Robust Error Handling

Handles missing fields

Handles invalid values

Retries form filling on failures

Logs all errors clearly

 6. Submission Reporting

Generates a submission_report.csv, containing:

Row number

Success/Failure

Error description

 7. Clean, Reusable Architecture

Modular functions

Separation of driver setup, selectors, and utilities

Easy to extend for new form types

# Project Structure

 hackathon/
├── auto_fill_form.py # Main script to run
├── config.json # Form-specific settings
├── data.csv # Dataset with names, emails, etc.
├── submission_report.csv # Automatically created after run
├── screenshots/ # Screenshots and demo (optional)
└── README.md # This file##

Requirements
- Python 3.8 or later
- Google Chrome installed
- Required Python packages:
pip install selenium pandas webdriver-manager

- How to Use
1) Prepare your data.csv file with the correct columns (e.g., Full Name, Institute Email ID, Roll Number).

2) config.json:

json
{
  "Hackathon Registration": {
    "url": "https://docs.google.com/forms/your-form-link"
  }
}

-Run via CLI:
python auto_fill_form.py --form "Hackathon Registration" --data "data.csv"



- Logic & Design
The script reads rows from the dataset and submits them to the Google Form.

It uses either config-based field mapping or matches fields in order as seen in the form.

Includes randomized delays and typing speed to simulate human input.

Captures success/failure for each row, and stores the result in submission_report.csv.

Skips rows with incomplete or missing data.

Designed to be modular so you can add Excel/JSON or GUI in future easily.


