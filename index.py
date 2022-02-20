from functions import enterDirectory, traverseDirectory, renameDirectory

def main():
    enDirectory = enterDirectory()
    directorys = traverseDirectory(enDirectory)
    renameDirectory(enDirectory, directorys)

if __name__ == '__main__': main()
