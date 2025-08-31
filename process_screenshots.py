import os
import subprocess
import sys
from datetime import datetime, timedelta

# --- CONFIGURATION ---
PROJECT_DIR = os.path.expanduser("~/Desktop/ScreenshotProcessor")
TEMP_EXPORT_DIR = os.path.join(PROJECT_DIR, "temp_exports")
FINAL_ARCHIVE_DIR = os.path.join(PROJECT_DIR, "archive")
APPLESCRIPT_EXPORT_PATH = os.path.join(PROJECT_DIR, "export_script.scpt")

# --- 1. SETUP ---
print("Setting up directories...")
os.makedirs(TEMP_EXPORT_DIR, exist_ok=True)
os.makedirs(FINAL_ARCHIVE_DIR, exist_ok=True)

# --- 2. BRUTE-FORCE EXPORT ---
print("Beginning brute-force export of ALL screenshots from the Smart Album.")
print("‼️ This will take a very long time and use a lot of temporary disk space. Please be patient. ‼️")
try:
    # Note: We are only passing the export path now
    result = subprocess.run(
        ["osascript", APPLESCRIPT_EXPORT_PATH, TEMP_EXPORT_DIR],
        check=True,
        capture_output=True,
        text=True,
        timeout=3600 # Set a long timeout of 1 hour for the massive export
    )
    print(f"✅ {result.stdout.strip()}")
except subprocess.CalledProcessError as e:
    print(f"❌ AppleScript Error: {e.stderr.strip()}")
    sys.exit()
except subprocess.TimeoutExpired:
    print("❌ Export timed out after 1 hour. The library may be too large to export at once.")
    sys.exit()

# --- 3. FILTER EXPORTED FILES IN PYTHON ---
print("\n---")
print("Export complete. Now filtering files by date...")
cutoff_timestamp = (datetime.now() - timedelta(days=365)).timestamp()
files_to_process = []
total_files = 0
deleted_count = 0

for filename in os.listdir(TEMP_EXPORT_DIR):
    total_files += 1
    filepath = os.path.join(TEMP_EXPORT_DIR, filename)
    
    # Check the file's modification time (a reliable timestamp after a fresh export)
    if os.path.getmtime(filepath) < cutoff_timestamp:
        files_to_process.append(filepath)
    else:
        # Delete the new files we don't need
        os.remove(filepath)
        deleted_count += 1
        
print(f"Kept {len(files_to_process)} files older than one year.")
print(f"Deleted {deleted_count} newer files to save space.")
print("---")

# The next phase of processing code will go here.
print("✅ Export and filtering complete. We are ready to process the final files.")
