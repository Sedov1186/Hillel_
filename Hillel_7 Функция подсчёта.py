import random
random_list = [random.randint(1, 10) for _ in range(200)]
count_dict = {num: sum(1 for x in random_list if x == num) for num in set(random_list)}
get_plural_form = lambda num: "раз" if num == 1 else "раза"
for num, count in sorted(count_dict.items()):
    print(f"Число {num} встречается в первоначальном списке {count} {get_plural_form(count)}")
