import csv
import os
import shutil
import sys

def copy_files(csv_file, source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if present

        for row in reader:
            file_name = row[0] + ".xls"  # Assuming the file names are in the first column

            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)

            try:
                shutil.copy2(source_path, destination_path)
                print(f"Successfully copied {file_name}")
            except FileNotFoundError:
                print(f"File not found: {file_name}")
            except Exception as e:
                print(f"Error occurred while copying {file_name}: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python file_copy.py csv_file source_folder destination_folder")
        sys.exit(1)

    csv_file = sys.argv[1]
    source_folder = sys.argv[2]
    destination_folder = sys.argv[3]

    copy_files(csv_file, source_folder, destination_folder)
