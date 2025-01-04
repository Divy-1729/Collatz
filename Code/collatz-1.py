def collatz_step(num):
    """Performs one step of the Collatz sequence."""
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

def parse_input(user_input):
    """Parses input that might be in the form of an exponent like '2^62'."""
    if '^' in user_input:
        base, exponent = user_input.split('^')
        return int(base) ** int(exponent)
    else:
        return int(user_input)

def collatz(n):
    """Checks the Collatz conjecture for all numbers from 1 to n."""
    for i in range(2, n + 1):  # Start from 2 since the conjecture trivially holds for 1.
        current = i
        while current != 1:
            current = collatz_step(current)
    print(f"The Collatz conjecture holds for all natural numbers greater than 1 up to {n}.")

user_input = input("Enter a number (supports exponents like 2^62): ")
n = parse_input(user_input)
collatz(n)
