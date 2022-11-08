#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Sep 2021
# This program multiplies each whole number that goes up to the users number


def main():
    # This function multiplies each whole number that goes up to the users number
    counter = 1
    factorial_product = 1

    # Input
    integer_as_string = input("\nEnter a positive number: ")

    # Process and Output
    try:
        integer_as_int = int(integer_as_string)
        if integer_as_int < 0:
            print("\nPlease enter a positive number. ")
        else:
            while counter <= integer_as_int:
                factorial_product = factorial_product * counter
                counter = counter + 1
            print(
                "\nThe product of all positive numbers from 1 to {0} is {1}.".format(
                    integer_as_string, factorial_product
                )
            )

    except Exception:
        print("\nInvalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
