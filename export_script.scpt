# FINAL PRODUCTION SCRIPT (Corrected Syntax)

on run {exportPath, y, m, d}
	set oldScreenshots to {}
	
	-- Manually construct the date to be 100% reliable
	set cutoffDate to (current date)
	set year of cutoffDate to y as integer
	set month of cutoffDate to m as integer
	set day of cutoffDate to d as integer
	set time of cutoffDate to 0 -- Sets it to the very beginning of that day
	
	tell application "Photos"
		set allScreenshots to (every media item in album "ScreenshotArchive")
		
		repeat with oneItem in allScreenshots
			try
				if (creation date of oneItem) < cutoffDate then
					set end of oldScreenshots to oneItem
				end if
			on error
				-- Silently skip any corrupt items
			end try
		end repeat
		
		-- === THIS ENTIRE BLOCK HAS BEEN MOVED INSIDE 'TELL' ===
		set itemsFound to count of oldScreenshots
		if itemsFound > 0 then
			export oldScreenshots to (POSIX file exportPath) with using originals
			return "SUCCESS: Exported " & itemsFound & " items."
		else
			return "SUCCESS: Found 0 items older than the cutoff date."
		end if
		-- === END OF MOVED BLOCK ===
		
	end tell
end run
