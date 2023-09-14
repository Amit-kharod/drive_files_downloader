import os
import csv
import gdown

# Function to convert Google Drive link to download link
def convert_to_download_link(drive_link):
    if "drive.google.com/file/d/" in drive_link:
        file_id = drive_link.split("/file/d/")[1].split("/")[0]
    elif "drive.google.com/open?id=" in drive_link:
        file_id = drive_link.split("/open?id=")[1]
    else:
        return None

    download_link = f"https://drive.google.com/uc?export=download&id={file_id}"
    return download_link

# Read the CSV file containing Google Drive links
csv_file = "links.csv"  # Replace with the path to your CSV file
output_folder = "rancho2"
start_line = 1

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    links = [row[0] for row in reader]

# Download files starting from line 35
for i, drive_link in enumerate(links[start_line - 1:], start=start_line):
    download_link = convert_to_download_link(drive_link)
    print(drive_link)
    
    if download_link:
        output_file = os.path.join(output_folder, f"{i}.jpg")
        gdown.download(download_link, output_file, quiet=False)
        print(f"Downloaded {output_file} from {drive_link}")
    else:
        print(f"Skipped invalid link: {drive_link}")
