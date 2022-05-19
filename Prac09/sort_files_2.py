"""
CP1404
Sort Files based on categorization
"""

import os


def main():
    """Move files to where user wants based on extenstions."""
    os.chdir("FilesToSort.zip")
    for file_name in os.listdir('.'):
        if os.path.isdir(file_name):
            continue

        extension = file_name.split('.')[-1]
        if extension not in extension_to_category:
            category = input(f"What Category would you like the {extension} files to be sorted into?")
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

            os.rename(f"{file_name}, {extension_to_category[extension]}/{file_name}")


main()
