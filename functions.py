from bullet import Input, colors, YesNo
from colored import fg, attr
from os import listdir, rename
from os.path import isdir, isfile
from getpass import getuser

colorRed = fg('#CC0000')
colorGreen = fg('#73D216')
colorBlue = fg('#338CFF')
res = attr('reset')

def err():
    print(f'{colorRed}Wrong data{res}')
    exit()

def validateDir(directory): 
    if not isdir(directory): err()
    else: return directory 

def enterDirectory():
    directory = Input(f'{colorGreen}Enter the directory {res}', default = f"/home/{getuser()}/Downloads", word_color = colors.foreground["yellow"]).launch()
    directory = validateDir(directory)
    return directory

def traverseDirectory(directory):
    directoryArray = listdir(directory)
    directorys = []

    dir_file = YesNo(f'{colorGreen}Do you want to rename the folders (y) or files (n)? {res}', default = 'n', word_color = colors.foreground["yellow"]).launch()

    print(f'Current name {colorBlue}::{res} New name')
    for file in directoryArray: 
        if dir_file is True:
            if  isdir(f'{directory}/{file}'): 
                print(f'{file} {colorRed}::{res} {file.title()}')
                directorys.append(file)
        else: 
            if  isfile(f'{directory}/{file}'): 
                print(f'{file} {colorRed}::{res} {file.title()}')
                directorys.append(file)

    return directorys, dir_file

def renameDirectory(directory, directorys, dir_file):
    dir_file = 'folders' if dir_file is True else 'files'
    renameQuestion = YesNo(f'{colorGreen}Do you want to rename the {dir_file}? {res}', default = 'n', word_color = colors.foreground["yellow"]).launch()

    if renameQuestion: 
        for name in directorys: rename(f'{directory}/{name}', f'{directory}/{name.title()}')
        print(f'{colorBlue}Renamed directories{res}')
    else: print(f'{colorRed}Directories not renamed{res}')
