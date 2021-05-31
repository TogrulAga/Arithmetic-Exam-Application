def check(string):
    if not string.isnumeric():
        print("It is not a number!")
    else:
        number = int(string)
        if number >= 202:
            print(number)
        else:
            print("There are less than 202 apples! You cheated on me!")
