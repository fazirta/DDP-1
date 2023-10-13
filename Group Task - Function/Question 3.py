def print_fibonacci_numbers(n):
    """
    Print the first N numbers of the Fibonacci sequence.
    """
    fibonacci_sequence = [1, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    print("Fibonacci Sequence:")
    print(*fibonacci_sequence[:n], sep=', ')

# Example usage:
N = 7
print_fibonacci_numbers(N)
