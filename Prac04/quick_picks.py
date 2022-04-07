"""
Quick Pick Program
"""

import random

NUM_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    """Choose Sets of Random Numbers"""
    num_quick_picks = int(input("How Many Quick Picks?: "))
    while num_quick_picks < 0:
        print("That Makes no Sense!")
        num_quick_picks = int(input("How Many Quick Picks?: "))

        for i in range(num_quick_picks):
            quick_pick = []
            for j in range(NUM_PER_LINE):
                number = random.randint(MIN, MAX)
                while number in quick_pick:
                    number = random.randint(MIN, MAX)
                quick_pick.append(number)
                quick_pick.sort()
                print("".join("{:2}".format(number) for number in quick_pick))
