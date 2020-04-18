import sys
import os
from PIL import Image

# grab first and second argument
cwd = os.getcwd()

try:
    folder_jpg = sys.argv[1]
    folder_png = sys.argv[2]

except IndexError as err:
    print("correct usage of script - provide 2 arguments - jpeg folder name and png folder name")
    exit()

def get_full_path(file_or_folder):
    if (len(file_or_folder) == 0):
        print("file or folder invalid")
        exit()
    return cwd + f"/{file_or_folder}"
# check if folder exists and if not, create it

path_to_jpg_folder = get_full_path(folder_jpg)
path_to_png_folder = get_full_path(folder_png)

if (not(os.path.isdir(path_to_jpg_folder))):
    print(f"jpg folder path not found in  {cwd}")
    exit()

print("creating png folder...")

try:
# Create target Directory
    os.mkdir(path_to_png_folder)
    print("Directory " , folder_png ,  " Created ") 
except FileExistsError:
    print("Directory " , folder_png ,  " already exists")
    proceed = input("Are you sure you want to continue? ")
    if (proceed.lower() == "n"):
        exit()

# loop through folder <first_arg>, convert images to png and save to new folder
jpeg_files = os.listdir(path_to_jpg_folder)
print(jpeg_files)

if (len(jpeg_files) == 0):
    print("There are no jpeg files to convert to png in the given folder")
    exit()

for jpeg_file in jpeg_files:
    jpeg_file_path = get_full_path(f"{folder_png}/{jpeg_file}")
    filename, file_extension = os.path.splitext(jpeg_file_path)
    
    if (file_extension == ".jpg" or file_extension == ".jpeg"):
        print(f"converting file {folder_jpg}/{jpeg_file} to {filename}.png")
    
        try:
            img = Image.open(f"./{folder_jpg}/{jpeg_file}")
            img.save(f"{filename}.png", "png")
        except FileNotFoundError as err:
            print("something went wrong >>", err)
            exit()
