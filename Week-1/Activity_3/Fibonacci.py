def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci series:")

    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

    print()


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


def main():
    n = int(input("Enter a number (N): "))

    fibonacci(n)

    answer = factorial(n)

    print("Factorial of", n, "is", answer)


if __name__ == "__main__":
    main()