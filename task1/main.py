def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if (n <= 0):
            return 0
        if (n == 1):
            return 1
        if (n in cache.keys()):
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def main():
    get_fibanacci_number = caching_fibonacci()

    while (True):
        user_input = input(
            "Enter fibonacci element order (type 'e' to stop exit): ")

        if (user_input.casefold() == "e"):
            print("Good Bye!")
            break
        if (not user_input.isdigit()):
            print("Please enter a number!")
            continue

        number = get_fibanacci_number(int(user_input))
        print(f"Your fibonacci number is {number}")


if __name__ == "__main__":
    main()
