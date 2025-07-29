import os

file_path = "text.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("The location doesnt exists")