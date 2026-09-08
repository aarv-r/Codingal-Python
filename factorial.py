def factorial(n):
    """We are calculating the factorial of a number."""
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial.__doc__)
print(factorial(5))
print(factorial(123))