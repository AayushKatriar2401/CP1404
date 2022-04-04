"""
Password Checker
"""
Min_Length = 2
Max_Length = 6
Special_Char_Required = False
Special_Char = "!@#$%^&*()_-= +`~,./ '[] <>?{}| \\"


def is_valid_password(password):
    if len(password) < Min_Length or len(password) > Max_Length:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        if char.isdigit():
            count_digit += 1

        elif char.islower():
            count_lower += 1

        elif char.isupper():
            count_upper += 1

        elif char in Special_Char:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
        if Special_Char_Required:
            if count_special == 0:
                return False
            return True


def main():
    print("Please enter a valid password")
    print(f"your password must be between {Min_Length} and {Max_Length} characters and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if Special_Char_Required:
            print("\tand 1 or more special characters: ", Special_Char)
            password = input("> ")
            while not is_valid_password(password):
                print("invalid password!")
                password = input("> ")
                print("Your" + str(len(password)) + "character password is valid" + password)
main()
