def is_odd(number):
    """Determine the given number is odd or not?"""
    if number % 2 == 0:
        return False
    else:
        return True

print(is_odd(7))
help(is_odd)