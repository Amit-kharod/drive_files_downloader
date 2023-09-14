import os
from PIL import Image

# Function to change the file extension based on size
def change_extension(file_path):
    try:
        file_size = os.path.getsize(file_path)  # Get file size in bytes
        if file_size < 1024 * 1024:  # Check if file size is less than 1 MB
            new_extension = ".pdf"
        else:
            new_extension = ".jpg"

        # Rename the file with the new extension
        base_name, _ = os.path.splitext(file_path)
        new_file_path = f"{base_name}{new_extension}"
        os.rename(file_path, new_file_path)
        print(f"Renamed {file_path} to {new_file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

# Directory containing the files
folder_path = "rancho2"  # Replace with your folder path

# Loop through files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        change_extension(file_path)

print("File extension changes completed.")
