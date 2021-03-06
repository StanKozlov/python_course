#!/usr/bin/python3.4
import argparse
import subprocess
import os.path
from shutil import copy, copytree, rmtree

parser = argparse.ArgumentParser(description='Script for looking for changes '
                                 'in file or in folder.')
parser.add_argument('command', choices=['store', 'diff'], type=str,
                    help='Store current state of file or folder ("store"), '
                         'or see what is changed ("diff")')
parser.add_argument('file', type=str, help='Path to file of interest')

args = parser.parse_args()
command = args.command
file = args.file
path = file.split('/')
filename = path[len(path)-1]

if command == 'store':
    if os.path.isfile(file):
        copy(file, "/home/hamster/PycharmProjects/untitled/sad/")
    elif os.path.isdir(file):
        folder = "/home/hamster/PycharmProjects/untitled/sad/" + filename
        if os.path.exists(folder):
            rmtree(folder)
            copytree(file, folder)
        else:
            copytree(file, folder)
    else:
        print('Sorry, please enter path to a file or a folder')
elif command == 'diff':
    operation = 'diff' + ' ' + file + ' ' + './sad/' + filename
    print(subprocess.call(operation, shell=True))
else:
    print('Sorry, repeat your command')
