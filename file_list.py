"""
We want to make a python program that will take all the files that are of chosen extensions and put them in 1 text file that will be in the same directory as the program.

Example:
we have a directory with 2 files and folder:
file1.txt
file2.txt
folder1: file3.txt

we want to take all the files that are of .txt & .json extension and put them in 1 text file that will be in the same directory as the program
that will look like this:

[strucutre of all the files and folders in the directory]

file1.txt:
[content of file1.txt]
file2.txt:
[content of file2.txt]
file3.txt:
[content of file3.txt]

* note that we will add also a ignore list that will ignore the files & folders that are in the ignore list
"""

import os
import sys


def get_files(directory, extensions, ignore_list):
    files = []
    for root, dirs, file_list in os.walk(directory):
        for file in file_list:
            if file not in ignore_list:
                for extension in extensions:
                    if file.endswith(extension):
                        files.append(os.path.join(root, file))
    return files


def write_project_structure(directory, output_file, ignore_list):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, "").count(os.sep)
        indent = " " * 4 * level
        output_file.write(f"{indent}{os.path.basename(root)}/\n")
        subindent = " " * 4 * (level + 1)
        for file in files:
            if file not in ignore_list:
                output_file.write(f"{subindent}{file}\n")


if __name__ == "__main__":
    directory = os.path.dirname(os.path.realpath(__file__))
    extensions = [".txt", ".json"]
    ignore_list = ["pytext.py", "output.txt"]
    files = get_files(directory, extensions, ignore_list)

    with open("output.txt", "w") as output_file:
        output_file.write("Project Structure:\n")
        write_project_structure(directory, output_file, ignore_list)
        output_file.write("\n")

        for file_path in files:
            output_file.write(f"{file_path}:\n")
            with open(file_path, "r") as input_file:
                content = input_file.read()
                output_file.write(content)
                output_file.write("\n\n")
