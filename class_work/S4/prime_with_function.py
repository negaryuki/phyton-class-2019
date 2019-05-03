def prime(i, number):
    is_prime = True
    while i < number-1:
    i = i + 1
    if number % i == 0:
        is_prime = False
    return is_prime


print(is_prime)
