def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


int_list = [6, 20, 15, 9]
functions = [min, max, len, sum, sorted]

result = apply_all_func(int_list, *functions)
for key, value in result.items():
    print(f"{key}: {value}")