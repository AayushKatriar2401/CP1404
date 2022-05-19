"""
CP1404
Sorting files based on extension
"""

import os


def main():
    """Move files into folders based on the name of their extensions"""
    os.chdir("FilesToSort.zip")
    for file_name in os.listdir('.'):
        if os.path.isdir(file_name):
            continue

        extension = file_name.split('.')[-1]

        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        os.rename(file_name, f"{extension}/{file_name}")
        print(f"{extension}/{file_name}")


main()
