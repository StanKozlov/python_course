#!/usr/bin/python3.4
import argparse
import subprocess
import os.path


parser = argparse.ArgumentParser(description='Compressing of the file')
parser.add_argument('percent', type=str,
                    help='Enter the ideal size of compression')
parser.add_argument('file', type=str, help='Path to file of interest')
parser.add_argument('--new_file', type=str, default=' ', help='Path to compressed file,'
                                                              'usage = --new_file path')

args = parser.parse_args()
percent = args.percent
file = args.file
new_file = args.new_file


def work_with_dir(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            filename = os.path.join(root, name)
            print(filename)
            if filename[-4:] == '.png' or filename[-4:] == '.jpg':
                operation = 'convert ' + filename + ' -resize ' + percent + '% ' + filename
                print(subprocess.call(operation, shell=True))

if os.path.exists(file):
    if new_file is not ' ':
        if os.path.isfile(file):
            operation = 'convert ' + file + ' -resize ' + percent + '% ' + new_file
            print(subprocess.call(operation, shell=True))
        else:
            print('I ignored your "new_file" path')
            work_with_dir(file)
    else:
        if os.path.isfile(file):
            operation = 'convert ' + file + ' -resize ' + percent + '% ' + file
            print(subprocess.call(operation, shell=True))
        else:
            work_with_dir(file)
else:
    print('Gimme a valid path')


