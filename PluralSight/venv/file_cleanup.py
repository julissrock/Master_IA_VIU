import os
folder = 'test'
entries = os.scandir(folder)
for entry in entries:
    if os.path.isfile(entry):
        print('file:', entry.name)
    elif os.path.isdir(entry):
        print('folder:', entry.name)