#this code maps the number of iterations it takes on average for each digit to reach 1
import matplotlib.pyplot as plt

def collatz_step(num):
    """Performs a single step of the Collatz sequence."""
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

def collatz_iterations_to_one(num):
    """Calculates the number of iterations in the Collatz sequence to reach 1."""
    c = 0  # Count the number of steps
    while num != 1:
        num = collatz_step(num)  # Perform the Collatz step
        c += 1  # Increment the step count
    return c  # Return the number of steps

def average_iterations_by_digit(limit):
    """Computes the average iterations for numbers grouped by ending digits (0-9)."""
    digit_iterations = {digit: [] for digit in range(10)}  # Store iterations for each digit

    for i in range(2, limit + 1):  # Start from 2 to exclude 1 as the starting number
        ending_digit = i % 10
        iterations = collatz_iterations_to_one(i)
        digit_iterations[ending_digit].append(iterations)

    # Compute the averages for each digit
    digit_averages = {
        digit: (sum(iterations) / len(iterations)) if iterations else 0
        for digit, iterations in digit_iterations.items()
    }
    return digit_averages

# Main execution
n = int(input("Enter your upper limit: "))
digit_averages = average_iterations_by_digit(n)

# Prepare data for plotting
digits = list(digit_averages.keys())
averages = list(digit_averages.values())

# Find the digits with max and min averages
max_digit = max(digit_averages, key=digit_averages.get)
min_digit = min(digit_averages, key=digit_averages.get)

# Display the results
plt.bar(range(len(digits)), averages, tick_label=digits)
plt.xlabel("Ending Digit")
plt.ylabel("Average Iterations to Reach 1")
plt.title(f"Average Iterations by Ending Digit (2 to {n})")

# Annotate the max and min values
plt.text(digits.index(max_digit), digit_averages[max_digit], f"Max\n{digit_averages[max_digit]:.2f}",
         ha='center', va='bottom', fontsize=10, color='green', weight='bold')
plt.text(digits.index(min_digit), digit_averages[min_digit], f"Min\n{digit_averages[min_digit]:.2f}",
         ha='center', va='top', fontsize=10, color='red', weight='bold')

plt.show()
