def is_power_of_four(number):
    if number <= 0:
        return False
    if (number & (number - 1)) != 0:
        return False
    return (number - 1) % 3 == 0

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
