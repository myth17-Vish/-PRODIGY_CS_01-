
import re

def assess_password_strength(password):
    length_score = 0
    letter_score = 0
    number_score = 0
    symbol_score = 0

    if len(password) < 12:
        length_score = 0
    else:
        length_score = 1

    if re.search(r'[A-Z]', password):
        letter_score = 1
    else:
        letter_score = 0

    if re.search(r'[a-z]', password):
        letter_score += 1
    else:
        letter_score = 0

    if re.search(r'\d', password):
        number_score = 1
    else:
        number_score = 0

    if re.search(r'[!@#$%^&*()\-+]', password):
        symbol_score = 1
    else:
        symbol_score = 0

    total_score = length_score + letter_score + number_score + symbol_score

    if total_score == 0:
        strength = "Very weak"
    elif total_score == 1:
        strength = "Weak"
    elif total_score == 2:
        strength = "Moderate"
    elif total_score == 3:
        strength = "Strong"
    else:
        strength = "Very strong"

    return strength

def main():
    while True:
        print("Password Strength Assessment Tool")
        print("1. Assess a password")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter a password to assess: ")
            strength = assess_password_strength(password)
            print("Password strength:", strength)

        elif choice == "2":
            print("Have a Nice try!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
