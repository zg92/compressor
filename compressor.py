import os, sys 
from PIL import Image

def filesList(filePath):
    return os.listdir(filePath)

def compressPhoto(file_to_edit, destination_directory):
    filepath = os.path.join(os.getcwd(),file)
    picture = Image.open(filepath)
    picture.save(os.path.join(destination_directory, file), "JPEG", optimize=True, quality=10)
    return

def compressProcess(file, destination_directory):
    files = filesList(filePath)
    for file_to_edit in files:
        compressPhoto(file_to_edit, destination_directory)

if __name__ == '__main__': 
    if sys.argv[1] or sys.argv[2] != None:
        compressProcess(sys.argv[1], sys.argv[2])
    else:
        print('Arguments supplied were invalid')

