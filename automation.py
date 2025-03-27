import os
import fnmatch
from tkinter.filedialog import askdirectory

# This is the path of the folder that the dialog box opens - it's the Zoom folder that contains each folder containing meeting screenshots 
zoom_path = r"C:\Users\Subbiahswamy\OneDrive\Documents\Zoom"

# dir_path1 holds the path name of the first folder, of which we will count the number of files 
dir_path1 = rf"{askdirectory(title="Select First Folder", initialdir=zoom_path, mustexist=True)}"
# dir_path2 holds the path name of the second folder, whose screenshots we're renaming 
dir_path2 = rf"{askdirectory(title="Select Second Folder", initialdir=zoom_path, mustexist=True)}"
newFolderName = os.path.basename(dir_path1)[:11] + input("Enter the name for your new single folder: ")
newFolderPath = os.path.join(zoom_path, newFolderName)


# This block of code below counts the number or files in the first folder, so we know how much to increase the numbers of the file names in the second folder by (number_before will be added to the number in the orginal filename)
pattern = 'Screenshot[*'
number_before = len(fnmatch.filter(os.listdir(dir_path1), pattern))
#print(f'The number of {pattern} files in {dir_path1} is {number_before}')




for item in os.listdir(dir_path2):
    #print(item)
    screenshot_num = ""
    for x in range(11,13):
        if item[x] == "]":
            break
        else:
            screenshot_num += item[x]
            screenshot_num = screenshot_num
    screenshot_num = int(screenshot_num)
    new_num = screenshot_num + number_before

    new_item = f"Screenshot[{new_num}]-01.png"
    try:
        os.rename(
            os.path.join(dir_path2, item),
            os.path.join(dir_path1, new_item)
        )
    except PermissionError:
        continue
    except Exception as e:
        raise Exception(e)
    #print(screenshot_num, item, new_num, new_item, "\n")


os.rename(dir_path1, newFolderPath)

"""
try:
    os.remove(dir_path2)
    print("% s removed successfully" % dir_path2)
except OSError as error:
    print(error)
    print("File path can not be removed")
"""