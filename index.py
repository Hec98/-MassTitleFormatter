from functions import enterDirectory, traverseDirectory, renameDirectory

def main():
    enDirectory = enterDirectory()
    (directorys, dir_file) = traverseDirectory(enDirectory)
    renameDirectory(enDirectory, directorys, dir_file)

if __name__ == '__main__': main()
