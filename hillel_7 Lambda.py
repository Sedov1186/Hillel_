check_even_odd = lambda num: "ноль" if num == 0 else "чётное" if num % 2 == 0 else "не чётное"
print(check_even_odd(0))    # Output: ноль
print(check_even_odd(7))    # Output: не чётное
print(check_even_odd(10))   # Output: чётное
