def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number =int(input("Enter a number: "))
candidate = number + 1
while True:
    if is_prime(candidate):
        print(f"The next prime number after {number} is {candidate}.")
        break
    candidate += 1
    