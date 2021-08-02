def run():
    factor = int(input('Number'))
    print(factorial(factor))

def factorial(n):
    print(n)
    if n == 1:
        return 1
    f = n * factorial(n-1)
    return f

if __name__ == '__main__':
    run()


# n = n*(n-1)