# Backup Details Generator for Windows

This utility provides a simple way to add backup details to file and directory paths in Windows. It appends a timestamp-based suffix to the original file name to create a backup copy.

This project was inspired by [arkenfox/user.js](https://github.com/arkenfox/user.js), which provides a hardened Firefox configuration. It uses a similar naming convention to store backups of configuration files.

## How it Works

The utility is implemented using Python and a Windows batch script. The Python script adds the backup details to file and directory paths, while the batch script allows you to run the Python script by dragging and dropping files onto it.

### Python Script

The Python script, `backup_details_generator.py`, contains the following functionalities:

- Imports the necessary libraries
- Defines the `add_backup_details()` function to append backup details to file and directory paths
- Performs the backup process by copying files or directories with added backup details

To use the script, run it from the command line with the file or directory paths as arguments.

### Batch Script

The batch script, `backup_details_generator.bat`, is a helper script that allows you to drag and drop files onto it. It passes the dropped file names as arguments to the Python script for processing.

## Usage

1. Ensure you have Python installed on your Windows system.
2. Copy the files `backup_details_generator.py` and `backup_details_generator.bat` to your preferred location.
3. To generate backups with added details, perform one of the following:
   - Run the `backup_details_generator.py` script from the command line, providing the file or directory paths as arguments.
   - Drag and drop files onto the `backup_details_generator.bat` script.

## Examples

Here are a few examples of how the utility works:

- Running the script from the command line:

  ```
  python backup_details_generator.py path/to/file.txt path/to/folder
  ```

- Dragging and dropping files onto the batch script:
- Drag and drop `file1.txt` and `file2.txt` onto `backup_details_generator.bat`.
- The backup copies will be created with the added details in the same directory.
