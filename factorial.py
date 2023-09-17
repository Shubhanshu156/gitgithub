def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
# input a number
n=int(input("Enter number"))
print("factorial of number ",n,factorial(n))
