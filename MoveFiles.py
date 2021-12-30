import os 
import glob 
import shutil
import pprint

pp = pprint.PrettyPrinter()

def create_directory(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


def move_files(source_directory, target_directory, file_types=''):
    total_files = []
    for dirpath, subdirnames, filenames in os.walk(source_directory):
        total_files += [os.path.join(dirpath, file) for file in filenames]


    total_files = [file for file in total_files if file.split('.')[-1] in file_types]

    for file in total_files:
        if os.path.exists(os.path.join(target_directory, file.split('\\')[-1])):
            print(f'{file} already exists in {target_directory}')
            continue
        print(f'Moving {file} to {target_directory}:\\')
        shutil.move(file, target_directory)

source_directory = os.path.join('D:\\', 'Photos')
target_directory = os.path.join('D:\\', 'Videos')
move_files(source_directory, target_directory, file_types='MOV MP4')

photos_source_dir = os.path.join('C:\\', 'Users', 'Kevin Vivian', 'Pictures')
# photos_source_dir = os.path.join('D:\\', 'Videos')
photos_target_dir = os.path.join('D:\\', 'Photos')
move_files(photos_source_dir, photos_target_dir, file_types='AAE PNG JPG HEIC')