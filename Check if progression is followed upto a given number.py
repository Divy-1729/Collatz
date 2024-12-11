#This code checks if the numbers in a range follow the unit-digit diagram described in the paper
# Predefined valid transitions for unit digits based on your updated diagram
valid_transitions = {
    1: [4],
    4: [2, 7],
    2: [1, 6],
    6: [3, 8],
    3: [0],  # 3 leads to 0
    0: [5, 0],  # 0 leads to both 5 and 0
    5: [6],
    8: [9, 4],
    7: [2],
    9: [8],
}


def collatz_step(num):
    """Performs one step of the Collatz sequence."""
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1


def validate_collatz_unit_digits_sequence(num):
    """Validates the Collatz unit digits sequence for a given number."""
    current = num
    while current != 1:
        current_unit_digit = current % 10
        next_num = collatz_step(current)
        next_unit_digit = next_num % 10

        # Check if the next unit digit is valid
        if next_unit_digit not in valid_transitions.get(current_unit_digit, []):
            print(f"Invalid transition: {current_unit_digit} -> {next_unit_digit}")
            return False  # Invalid transition detected

        current = next_num
    return True


def validate_all_numbers_upto_n(n):
    """Validates Collatz unit digits sequence for all numbers from 1 to n."""
    for num in range(1, n + 1):
        if not validate_collatz_unit_digits_sequence(num):
            return False, num  # Return the first invalid number
    return True, None  # All numbers are valid


# Main execution
n = int(input("Enter the upper bound for your range: "))
is_valid, invalid_num = validate_all_numbers_upto_n(n)

if is_valid:
    print(f"All numbers up to {n} follow the unit digit algorithm.")
else:
    print(f"The number {invalid_num} does not follow the unit digit algorithm.")
