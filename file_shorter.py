import os, shutil
path = r'C:/Users/sc/OneDrive/Documents/python practice/automatic file shorter/'

file_name = os.listdir(path)

# get unique extensions
extensions = set()

for file in file_name:
    if os.path.isfile(path + file):
        ext = os.path.splitext(file)[1].lstrip('.')
        if ext:
            extensions.add(ext)
    

# create folders for each extension
for ext in extensions:
    folder = path + ext + " " + 'files/'
    if not os.path.exists(folder):
        os.makedirs(folder)

# move files to their respective folders 
for file in file_name:
    if os.path.isfile(path + file):
        ext = os.path.splitext(file)[1].lstrip('.')
        if ext:
            folder = path + ext + " " + 'files/'
            shutil.move(path + file, folder + file)
        
