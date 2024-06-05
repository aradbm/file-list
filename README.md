# File List

For ChatGPT and Claude.

## Instructions

1. Change the following lines

   ```python
       extensions = [".txt", ".json"]
       ignore_list = ["pytext.py", "output.txt"]
   ```

2. Run the script using Python:

   ```bash
   python file_list.py
   ```

3. The output will be saved in `output.txt` in the same directory as the script.

## Example output:

    ```txt
    Project Structure:
    test folder/
        file1.txt
        file2.txt
        folder1/
            file3.txt

    D:\Downloads\test folder\file1.txt:
    description1

    D:\Downloads\test folder\file2.txt:
    description2

    D:\Downloads\test folder\folder1\file3.txt:
    description3
    ```
