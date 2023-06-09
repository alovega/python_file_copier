# File Copy Script

This script copies files from a source folder to a destination folder based on a CSV file.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository or download the script file `file_copy.py`.

2. Install the required dependencies by running the following command:

## Usage

1. Prepare a CSV file with the list of file names to copy. The CSV file should have one column containing the file names. Place this file in the same directory as the script.

2. Open a terminal or command prompt and navigate to the directory containing the `file_copy.py` script.

3. Run the following command:

```

python file_copy.py files_to_copy.csv path/to/source/folder path/to/destination/folder 

```

Replace `csv_file` with the name of your CSV file, `source_folder` with the path to the source folder containing the files to copy, and `destination_folder` with the path to the destination folder where the files should be copied to.

For example:
If the destination folder does not exist, it will be created automatically.
4. The script will read the CSV file, copy the specified files from the source folder to the destination folder, and display the status of each file copy operation.

## Example CSV File Format

The CSV file should have the following format:

Please note that the file names should be provided in a single column without any headers.

## License

This project is licensed under the [MIT License](LICENSE).
