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

 ```
 Project Structure:
   file list/
       output_20240606_025408.txt
       README.md
       example_folder/
           file1.txt
           file2.txt
           python_file.py
           folder1/
               file3.txt
   
   D:\Downloads\file list\example_folder\file1.txt:
   description1
   
   D:\Downloads\file list\example_folder\file2.txt:
   description2
   
   D:\Downloads\file list\example_folder\python_file.py:
   ##Example python file
   import os
   
   print("Hello, World!")
   
   
   D:\Downloads\file list\example_folder\folder1\file3.txt:
   description3
 ```
