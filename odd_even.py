try:
    while True:
        a = int(input("What number are you thinking?\n"))
        if a % 2 == 0:
            print("That's an even number! Have another?")
        else:
            print("That's an odd number! Have another?")
except ValueError:
    print('Please enter integer values')
