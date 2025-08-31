# FINAL SCRIPT (Brute-Force Export)
# Exports EVERYTHING from the Smart Album without any filtering.

on run {exportPath}
	tell application "Photos"
		try
			set allScreenshots to (every media item in album "ScreenshotArchive")
			
			if (count of allScreenshots) is 0 then
				return "ERROR: The 'ScreenshotArchive' album is empty."
			end if
			
			export allScreenshots to (POSIX file exportPath) with using originals
			
			return "SUCCESS: Exported " & (count of allScreenshots) & " total items for filtering."
		on error errMsg
			return "ERROR: Failed during export. " & errMsg
		end try
	end tell
end run
