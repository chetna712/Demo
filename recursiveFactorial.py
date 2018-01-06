def factorial(n):
    "This is a recursive function to find factorial of a number"
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)


n = int(raw_input("Enter number:"))

print factorial(n)
