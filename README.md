# 🤖 Google Form Auto-Filler with Dynamic Mapping

This project automates the process of filling and submitting Google Forms using data from CSV files. It supports **multiple forms**, **custom field mapping**, **error handling**, **submission reporting**, and **human-like delays**, all through a simple **command-line interface (CLI)** and a config file.

---
The link to the drive containing demo video-https://drive.google.com/drive/folders/1xI3vgPXohF3sRYew7eBHCDHN9vkZ5tKv

## ✅ Features

- 🔗 **Support for Multiple Forms** using a `config.json`
- 🔀 **Dynamic Field Mapping** (manual or automatic by order)
- 📥 **Dataset Input via CSV** (Excel/JSON-ready)
- ❗ **Error Handling** for missing or invalid entries
- 📊 **Submission Status Reporting** (`submission_report.csv`)
- ⏱️ **Human-Like Random Delays** between actions
- 💻 **CLI Interface** for simple execution
- 🧠 **Optional Field Auto-Detection** when config not provided

---

## 📂 Project Structure

📁 hackathon/
├── auto_fill_form.py # Main script to run
├── config.json # Form-specific settings
├── data.csv # Dataset with names, emails, etc.
├── submission_report.csv # Automatically created after run
├── screenshots/ # Screenshots and demo (optional)
└── README.md # This file##

🔧 Requirements
- Python 3.8 or later
- Google Chrome installed
- Required Python packages:
pip install selenium pandas webdriver-manager

- How to Use
✅ Prepare your data.csv file with the correct columns (e.g., Full Name, Institute Email ID, Roll Number).

✅ config.json:

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


