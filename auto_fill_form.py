import argparse
import pandas as pd
import time
import random
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ----- CLI ARGUMENT PARSING -----
parser = argparse.ArgumentParser()
parser.add_argument("--form", required=True, help="Form name as defined in config.json")
parser.add_argument("--data", required=True, help="Path to CSV file")
args = parser.parse_args()

# ----- LOAD CONFIG -----
with open("config.json") as f:
    config = json.load(f)

form_config = config.get(args.form)
if not form_config:
    print(f"[✗] No form found in config with name '{args.form}'")
    exit(1)

form_url = form_config["url"]
field_mapping = form_config.get("field_mapping")  # Might be None

# ----- LOAD CSV -----
df = pd.read_csv(args.data)
report = []

print(f"\n➡️ Processing form: {args.form}\n")

for index, row in df.iterrows():
    try:
        # Check for missing required fields
        if pd.isna(row.get("Full Name")) or pd.isna(row.get("Institute Email ID")) or pd.isna(row.get("Roll Number")):
            raise ValueError("Missing required data.")

        # Setup Chrome driver
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(form_url)
        time.sleep(random.uniform(1.5, 2.5))  # Dynamic delay

        if field_mapping:
            # Use label-based XPath
            for label, column_name in field_mapping.items():
                value = str(row.get(column_name, "")).strip()
                if value:
                    input_box = driver.find_element(
                        By.XPATH,
                        f"//div[contains(text(),'{label}')]/ancestor::div[@role='listitem']//input | "
                        f"//div[contains(text(),'{label}')]/ancestor::div[@role='listitem']//textarea"
                    )
                    for char in value:
                        input_box.send_keys(char)
                        time.sleep(random.uniform(0.05, 0.2))  # Human-like typing
        else:
            # Use index-based filling
            inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
            inputs[0].send_keys(row["Full Name"])
            inputs[1].send_keys(row["Institute Email ID"])
            inputs[2].send_keys(row["Roll Number"])

        # Submit
        submit_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Submit')]")
        submit_btn.click()

        report.append({"Name": row["Full Name"], "Status": "Submitted ✅"})
        print(f"[✓] Submitted for: {row['Full Name']}")
        time.sleep(1)
        driver.quit()

    except Exception as e:
        name = row.get("Full Name", "Unknown")
        report.append({"Name": name, "Status": f"Failed ❌ — {str(e)}"})
        print(f"[✗] Failed for: {name} — {e}")
        try:
            driver.quit()
        except:
            pass

# ----- EXPORT REPORT -----
try:
    report_df = pd.DataFrame(report)
    report_df.to_csv("submission_report.csv", index=False)
    print("\n📄 Submission report saved as submission_report.csv")
except Exception as e:
    print(f"\n⚠️ Could not save submission report: {e}")
