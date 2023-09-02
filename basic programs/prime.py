def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
n = int(input("Enter a number: "))

if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
