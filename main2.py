def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

input("Factorial-n! = nx (n-1)x...x 1 base case: 0! = 1. Press Enter")
print(" 4! =",factorial(4),"=4x3x2x1")
print(" 5! =", factorial(5)," = 5x4x3x2x1")

n= int(input("Enter a number (try 3 or 6):"))
guess = input("What is " + str(n) + " !? ")
input("n! = n x factorial(n-1) base case: 0! = 1.Press Enter")
print(" ", str(n) + "! = ",factorial(n)," your guess:",guess)