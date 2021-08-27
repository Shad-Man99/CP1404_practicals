finished = False
result = 0
while not finished:
    try:
        integer = int(input("Enter the integer: "))
        # TODO: this line

    except:  # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", integer)