import os 
import glob 
import shutil
import pprint

pp = pprint.PrettyPrinter()

def create_directory(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

file_types = 'MOVMP4'
# source_directory = os.path.join('D:\\', 'Photos')
source_directory = os.path.join('C:\\', 'Users', 'Kevin Vivian', 'Pictures')
target_directory = os.path.join('D:\\', 'Videos')

total_files = []
for dirpath, dirnames, filenames in os.walk(source_directory):
    total_files += [os.path.join(dirpath, file) for file in filenames]

total_files = [file for file in total_files if file.split('.')[-1] in file_types]

for file in total_files:
    if os.path.exists(os.path.join(target_directory, file.split('\\')[-1])):
        print(f'{file} already exists in {target_directory}')
        continue
    print(f'Moving {file} to {target_directory}:\\')
    shutil.move(file, target_directory)
