try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
if denominator = 0:
    print ("Enter a value larger than 0")


# 1. A ValueError will occur when non-numerical values are entered e.g. t,u or & would all yield a ValueError.
# 2. A ZeroDivisionError will occur when 0 is entered as a denominator as it is mathematically impossible to divide anything by 0.
# 3.