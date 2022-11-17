def factorial_iterative(n):
    prod = 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        for i in range(n):
            prod = prod*(i+1)
        return prod

number = int(input('Enter a number: '))
print(factorial_iterative(number))

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

num2 = int(input('Enter a number: '))
print(factorial_recursive(num2))

