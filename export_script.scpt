# FINAL SCRIPT: Targets "ScreenshotArchive" and uses a robust date check.

on run {exportPath, dateString}
	set exportFolder to POSIX file exportPath
	set cutoffDate to date dateString
	set oldScreenshots to {}
	
	tell application "Photos"
		set allScreenshots to (every media item in album "ScreenshotArchive")
		
		repeat with oneItem in allScreenshots
			try
				if (creation date of oneItem) < cutoffDate then
					set end of oldScreenshots to oneItem
				end if
			on error
				-- Skip any corrupted items
			end try
		end repeat
		
		if (count of oldScreenshots) is 0 then
			return "No screenshots found in the 'ScreenshotArchive' album older than the cutoff date."
		end if
		
		export oldScreenshots to exportFolder with using originals
	end tell
	
	return "Export complete."
end run
