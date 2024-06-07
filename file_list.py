import os
import datetime


def get_files(directory, extensions, ignore_list):
    files = []
    for root, dirs, file_list in os.walk(directory):
        # Exclude hidden directories and files
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        file_list = [f for f in file_list if not f.startswith(".")]

        # Check if the current directory is in the ignore list
        if os.path.basename(root) in ignore_list:
            dirs[:] = []  # Clear the dirs list to skip subdirectories
            continue

        for file in file_list:
            if file not in ignore_list:
                for extension in extensions:
                    if file.endswith(extension):
                        files.append(os.path.join(root, file))
    return files


def write_project_structure(directory, output_file, ignore_list):
    for root, dirs, files in os.walk(directory):
        # Exclude hidden directories and files
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        files = [f for f in files if not f.startswith(".")]

        # Check if the current directory is in the ignore list
        if os.path.basename(root) in ignore_list:
            dirs[:] = []  # Clear the dirs list to skip subdirectories
            continue

        level = root.replace(directory, "").count(os.sep)
        indent = " " * 4 * level
        output_file.write(f"{indent}{os.path.basename(root)}/\n")
        subindent = " " * 4 * (level + 1)
        for file in files:
            if file not in ignore_list:
                output_file.write(f"{subindent}{file}\n")


if __name__ == "__main__":
    directory = os.path.dirname(os.path.realpath(__file__))
    extensions = [".js", ".yml"]
    ignore_list = ["node_modules", "venv", "output.txt"]
    files = get_files(directory, extensions, ignore_list)

    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"output_{timestamp}.txt"

    with open(output_filename, "w") as output_file:
        output_file.write("Project Structure:\n")
        write_project_structure(directory, output_file, ignore_list)
        output_file.write("\n")

        for file_path in files:
            output_file.write(f"{file_path}:\n")
            with open(file_path, "r") as input_file:
                content = input_file.read()
                output_file.write(content)
                output_file.write("\n\n")
