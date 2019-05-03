# Method 1
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Method 2
def is_prime2(m):
    result = True
    for i in range(2, m):
        if m % i == 0:
            result = False
    return result


print(is_prime(12))
