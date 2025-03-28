#!/usr/bin/env python3

# Created By: Amara Tie

# Date: March 28, 2025

# This is a dating program where you have to be greater than 25 but younger than 40


def main():

    # Ask User for age
    age_as_string = input("Enter your age :")
    print("")

    # Check if the user's age matches the grandparents' criteria
    try:
        age_as_number = int(age_as_string)
        if age_as_number >= 25 and age_as_number <= 40:
            print("You are {}. You can date my grandchild".format(age_as_number))
        else:
            print("You are {}. You cannot date my grandchild".format(age_as_number))
    except Exception:
        print("This is not an age")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
