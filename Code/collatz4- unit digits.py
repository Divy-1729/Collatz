import matplotlib.pyplot as plt
def collatz_step(num):
    """Performs a single step of the Collatz sequence."""
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

def collatz_unit_digits(num):
    """Calculates the number of iterations in the Collatz sequence for a number."""
    original_num = num  # Store the original number
    c = 0  # Count the number of steps
    while num%10 != 1:
        num = collatz_step(num)  # Perform the Collatz step
        c += 1  # Increment the step count
    return c  # Return the number of steps

# Main execution
n = int(input("Enter your upper limit: "))
iteration = {}  # Dictionary to store the iterations for each number

for i in range(2, n + 1):
    iteration[i] = collatz_unit_digits(i)  # Compute and store iterations for each number

plt.plot(range(2, n + 1), iteration.values())
plt.xlabel("Numbers")
plt.ylabel("No of iterations to reach a number ending in 1")
plt.show()
