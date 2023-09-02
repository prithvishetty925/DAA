def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
n = int(input("Enter a number: "))

if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
