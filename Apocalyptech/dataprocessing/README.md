How to use bl3-dialogue-guid.py:

bl3-dialogue-guid.py <path to a DialogScript file with either .uasset / .uexp / .json* extension>

The JSON file needs to be created using the john-wick-parse.exe (for example, by using `john-wick-parse.exe serialize DialogScript_Recruitment` – don't include the file extension; just name is enough). If you don't want to manually generate the JSON files, just provide .uasset /.uexp file to `bl3-dialogue-guid.py` and the program should take care of it.
NOTE: The `john-wick-parse.exe` exe file needs to be in the same folder as the `.py` script.

*** for /r "C:\Users\Przemo\Downloads\Other\FModel\Output\Exports\OakGame (DialogScripts)" %i in (DialogScript*.uasset) do bl3-dialogue-guid.py "%i" > "%~dpni.txt"

--

Various data-processing scripts, used to drive data generation for various
Google Sheets, my refs database, and a mod or two (before I started pulling
that into the mod-generation scripts themselves).

These scripts will invariably need access to the `bl3data` and/or
`bl3hotfixmod` libraries which up in the main `python_mod_helpers` folder
in this repo, so you'll have to symlink or copy them over in order to make
use of the scripts in here.

