def collatz():
    try:
        number = int(input("Choose a Number: >> "))
        while number != 1:
            if (number % 2) == 0:
                number = number/2
                print(number)
            else:
                number = 3 * number + 1
                print(number)
    except ValueError:
        print("You did not enter an integer. Please try again.")
        collatz()

collatz()
