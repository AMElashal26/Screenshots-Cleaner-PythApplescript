# This script exports screenshots OLDER THAN a specific date (using metadata)

on run {exportPath, dateString}
	set exportFolder to POSIX file exportPath
	set cutoffDate to date dateString
	set oldScreenshots to {}
	
	tell application "Photos"
		-- 1. Get ALL media items where the 'screenshot' metadata flag is true
		set allScreenshots to (every media item whose screenshot is true)
		
		-- 2. Loop through them one by one
		repeat with oneItem in allScreenshots
			try
				-- 3. Check the date of each item individually
				if (creation date of oneItem) < cutoffDate then
					-- 4. If it's old, add it to our list
					set end of oldScreenshots to oneItem
				end if
			on error
				-- If an error occurs, skip the broken item.
			end try
		end repeat
		
		if (count of oldScreenshots) is 0 then
			return "No screenshots found before the specified date."
		end if
		
		-- 5. Export only the items from our final list
		export oldScreenshots to exportFolder with using originals
	end tell
	
	return "Export complete."
end run
