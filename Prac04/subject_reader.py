"""
Subject Reader
"""

FILENAME = "subject_data.txt"


def main():
    """Read and Display Subject"""
    data = get_data()
    display_subjects(data)


def get_data():
    """Read Data from the File Formatted"""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        data.append(parts)
    input_file.close()
    return data


def display_subjects(data):
    """Display Subject Data"""
    for subject_data in data:
        print("{} is taught by {:12} and has {:3} students".format(*subject_data))
