number = 101
i = 1
is_prime = True
while i < number-1:
    i = i + 1

    if number % i == 0:
        is_prime = False

print(is_prime)
