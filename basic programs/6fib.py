def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

# Example: Print the first 10 Fibonacci numbers
n = 10
fib_numbers = fibonacci(n)
print(fib_numbers)
