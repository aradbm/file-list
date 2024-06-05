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
