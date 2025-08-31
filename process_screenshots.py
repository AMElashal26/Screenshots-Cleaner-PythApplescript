import os
import subprocess
from PIL import Image
import pytesseract
from datetime import datetime, timedelta # Import datetime tools

# --- CONFIGURATION ---
PROJECT_DIR = os.path.expanduser("~/Desktop/ScreenshotProcessor")
TEMP_EXPORT_DIR = os.path.join(PROJECT_DIR, "temp_exports")
FINAL_ARCHIVE_DIR = os.path.join(PROJECT_DIR, "archive")
APPLESCRIPT_EXPORT_PATH = os.path.join(PROJECT_DIR, "export_script.scpt")

# --- 1. SETUP FOLDERS AND CALCULATE DATE ---
print("Setting up directories...")
os.makedirs(TEMP_EXPORT_DIR, exist_ok=True)
os.makedirs(FINAL_ARCHIVE_DIR, exist_ok=True)

# Calculate the cutoff date (one year ago)
cutoff_date = datetime.now() - timedelta(days=365)
# Format it for AppleScript: "Sunday, August 31, 2025 at 03:23:41 AM"
date_string_for_applescript = cutoff_date.strftime('%A, %B %d, %Y at %I:%M:%S %p')
print(f"Archiving screenshots created before: {date_string_for_applescript}")


# --- 2. RUN APPLESCRIPT TO EXPORT PHOTOS ---
print("Exporting screenshots from Photos. This may take a moment...")
try:
    # We now pass TWO arguments to the script: the path and the date string
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

# More code will go here...