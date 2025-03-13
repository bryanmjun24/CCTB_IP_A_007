import sys

def is_valid_integer_list(values):
    """Check if all values are integers."""
    try:
        return [int(value) for value in values.split(",")]
    except ValueError:
        return None

def perform_bitwise_operations(numbers):
    """Perform AND, OR, XOR on a list of numbers."""
    bitwise_and = numbers[0]
    bitwise_or = numbers[0]
    bitwise_xor = numbers[0]

    for num in numbers[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num

    return bitwise_and, bitwise_or, bitwise_xor

def filter_numbers(numbers, threshold):
    """Filter numbers greater than the threshold."""
    return [num for num in numbers if num > threshold]

if __name__ == "__main__":
    print("Content-Type: text/html\n")

    if len(sys.argv) < 3:
        print("<p>Error: Missing input values.</p>")
        sys.exit(1)

    numbers_input = sys.argv[1]
    threshold_input = sys.argv[2]

    numbers = is_valid_integer_list(numbers_input)
    if numbers is None:
        print("<p>Error: Please enter a valid list of integers separated by commas.</p>")
        sys.exit(1)

    try:
        threshold = int(threshold_input)
    except ValueError:
        print("<p>Error: Threshold must be an integer.</p>")
        sys.exit(1)

    if not numbers:
        print("<p>Error: No valid numbers provided.</p>")
        sys.exit(1)

    bitwise_and, bitwise_or, bitwise_xor = perform_bitwise_operations(numbers)
    filtered_numbers = filter_numbers(numbers, threshold)

    print(f"<h2>Results:</h2>")
    print(f"<p>Bitwise AND: {bitwise_and}</p>")
    print(f"<p>Bitwise OR: {bitwise_or}</p>")
    print(f"<p>Bitwise XOR: {bitwise_xor}</p>")
    print(f"<p>Numbers greater than threshold ({threshold}): {filtered_numbers}</p>")
