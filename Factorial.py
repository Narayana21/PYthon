# finding factorial of a number
def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)
num=int(input("Enter a number: "))
print("Factorial of",num," is",factorial(num))


# factorial of given number using inbuilt function
import math
num = 5
print("Factorial of", num, "is",math.factorial(num))