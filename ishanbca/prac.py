def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
            return n * factorial(n - 1)
n = int(input("enter a number"))
if n < 0:
    print("can't calculate factorial of negitive number")
else:
    result = factorial(n)
    print(f"the factorial of {n} is {result}")

   

