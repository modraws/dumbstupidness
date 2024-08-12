REM Step 3.5: Run custom preset scripts
cls
echo Making sure your custom presets are installed
python "%~dp0custompresetlist.py"
REM If you plan to add another list of custom presets, place it below this message like so.
REM python "%~dp0 name of your listing.py"
REM Be sure to remove the REM in front of this message, should you copy and paste it :)
python "%~dp0dumbstupidness.py"
echo Fleasion may update (a message saying "Updated fleasion.py to XXX" will show up in that case). If that happens, restart run.bat, as the custom presets won't apply!
timeout /t 5