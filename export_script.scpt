# FINAL SCRIPT: Targets the "ScreenshotArchive" Smart Album

on run {exportPath, dateString}
	set exportFolder to POSIX file exportPath
	set cutoffDate to date dateString
	set oldScreenshots to {}
	
	tell application "Photos"
		-- 1. Get every item from our new Smart Album
		-- This is the only line that needed a major change.
		set allScreenshots to (every media item in album "ScreenshotArchive")
		
		-- 2. Our robust loop checks the date of each item found
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
		
		-- 3. Export the final list
		export oldScreenshots to exportFolder with using originals
	end tell
	
	return "Export complete."
end run
