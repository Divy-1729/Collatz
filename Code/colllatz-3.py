def collatz_step(num):
    """Performs one step of the Collatz sequence."""
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

def collatz(n):
    """Checks the Collatz conjecture for all numbers from 1 to n using efficient memoization."""
    memo = {1: 0}  # Base case: 1 takes 0 steps to reach 1

    for i in range(2, n + 1):
        current = i
        steps = 0
        # Track the sequence we encounter to update memoization later
        sequence = []

        # Compute the Collatz sequence for current i
        while current not in memo:
            sequence.append(current)
            if current % 2 == 0:
                current = current // 2
            else:
                current = 3 * current + 1
            steps += 1

        # Once we find a number in the memo, we can update the whole sequence
        total_steps = steps + memo[current]

        # Add the sequence of numbers to memo with their calculated steps
        for idx, num in enumerate(sequence):
            memo[num] = total_steps - idx

    print(f"The Collatz conjecture holds for all natural numbers greater than 1 up to {n}.")

# Main execution without parse_input
n = int(input("Enter a number: "))
collatz(n)

