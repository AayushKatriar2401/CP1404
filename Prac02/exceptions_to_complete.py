"""
Exceptions to Complete
"""
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter integer: "))
        is_finished = True

    except ValueError:
        print("Please enter a valid integer!")
        print(f"Valid result is {result}")
