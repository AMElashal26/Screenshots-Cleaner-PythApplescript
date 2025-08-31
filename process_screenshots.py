import os
import subprocess
import sys
from datetime import datetime, timedelta

# --- CONFIGURATION ---
PROJECT_DIR = os.path.expanduser("~/Desktop/ScreenshotProcessor")
TEMP_EXPORT_DIR = os.path.join(PROJECT_DIR, "temp_exports")
FINAL_ARCHIVE_DIR = os.path.join(PROJECT_DIR, "archive")
APPLESCRIPT_EXPORT_PATH = os.path.join(PROJECT_DIR, "export_script.scpt")

# --- 1. SETUP & CALCULATE DATE COMPONENTS ---
print("Setting up directories...")
os.makedirs(TEMP_EXPORT_DIR, exist_ok=True)
os.makedirs(FINAL_ARCHIVE_DIR, exist_ok=True)

cutoff_date = datetime.now() - timedelta(days=365)
year_str = str(cutoff_date.year)
month_str = str(cutoff_date.month)
day_str = str(cutoff_date.day)

print(f"Searching for screenshots created before: {day_str}/{month_str}/{year_str}")

# --- 2. RUN APPLESCRIPT TO EXPORT PHOTOS ---
print("Exporting screenshots from Photos. This may take a significant amount of time...")
try:
    # Pass year, month, and day as separate arguments
    result = subprocess.run(
        ["osascript", APPLESCRIPT_EXPORT_PATH, TEMP_EXPORT_DIR, year_str, month_str, day_str],
        check=True,
        capture_output=True,
        text=True
    )
    # Print the success message returned from AppleScript
    print(f"✅ {result.stdout.strip()}")

except subprocess.CalledProcessError as e:
    print(f"❌ AppleScript Error: {e.stderr.strip()}")
    sys.exit() # Stop the script if export fails

# The next phase of processing code will go here.
print("---")
print("Next, we will process these exported files.")
