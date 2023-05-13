@ECHO OFF
REM pass (by reference) dropped file name to python script (source: https://stackoverflow.com/questions/51867874/run-command-with-drag-and-drop-onto-batch-file)
py backup_details_generator.py %*
REM pause