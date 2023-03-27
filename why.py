def is_power_of(number, base):
    # Base case: when number is smaller than base.
    number = number/base
    if number < base:
# If number is equal to 1, it's a power (base**0).
        return False
    else:
        return True
    return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
