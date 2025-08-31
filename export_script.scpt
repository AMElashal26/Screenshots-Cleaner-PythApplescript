# This script exports screenshots OLDER THAN a specific date (final, robust version)

on run {exportPath, dateString}
	set exportFolder to POSIX file exportPath
	set cutoffDate to date dateString
	set oldScreenshots to {}
	
	tell application "Photos"
		set allScreenshots to (every media item in album "Screenshots")
		
		repeat with oneItem in allScreenshots
			try
				-- Attempt to check the date. This might fail on a corrupted item.
				if (creation date of oneItem) < cutoffDate then
					set end of oldScreenshots to oneItem
				end if
			on error
				-- If an error occurs, do nothing and let the loop continue.
				-- This effectively skips the broken item.
			end try
		end repeat
		
		if (count of oldScreenshots) is 0 then
			return "No screenshots found before the specified date."
		end if
		
		export oldScreenshots to exportFolder with using originals
	end tell
	
	return "Export complete."
end run
