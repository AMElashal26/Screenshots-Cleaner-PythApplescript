import os
import subprocess
from PIL import Image
import pytesseract
from datetime import datetime, timedelta

# --- CONFIGURATION ---
PROJECT_DIR = os.path.expanduser("~/Desktop/ScreenshotProcessor")
TEMP_EXPORT_DIR = os.path.join(PROJECT_DIR, "temp_exports")
FINAL_ARCHIVE_DIR = os.path.join(PROJECT_DIR, "archive")
# We will use the final, production AppleScript now
APPLESCRIPT_EXPORT_PATH = os.path.join(PROJECT_DIR, "export_script.scpt")

# --- 1. SETUP FOLDERS AND CALCULATE DATE ---
print("Setting up directories...")
os.makedirs(TEMP_EXPORT_DIR, exist_ok=True)
os.makedirs(FINAL_ARCHIVE_DIR, exist_ok=True)

# Calculate the cutoff date (one year ago)
cutoff_date = datetime.now() - timedelta(days=365)
# THIS IS THE ONLY LINE THAT CHANGES: Format as ISO 8601
date_string_for_applescript = cutoff_date.strftime('%Y-%m-%dT%H:%M:%S')
print(f"Archiving screenshots created before: {date_string_for_applescript}")


# --- 2. RUN APPLESCRIPT TO EXPORT PHOTOS ---
print("Exporting screenshots from Photos. This may take a moment...")
try:
    subprocess.run(
        ["osascript", APPLESCRIPT_EXPORT_PATH, TEMP_EXPORT_DIR, date_string_for_applescript],
        check=True,
        capture_output=True,
        text=True
    )
    print("✅ Screenshots exported successfully.")
except subprocess.CalledProcessError as e:
    print(f"❌ AppleScript Error: {e.stderr}")
    exit()

# We will add the processing code in the next step...
