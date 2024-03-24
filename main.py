def sum_fun(a: int, b: int) -> int:
    return a + b


def multiply_fun(a: int, b: int) -> int:
    return a * b

def division_fun(a: int, b: int) -> int:
    return a / b


num_1 = int(input("Enter First Number =>"))
num_2 = int(input("Enter Second Number =>"))

sum_result = sum_fun(a=num_1, b=num_2)


division_result = sum_fun(a=num_1, b=num_2)
print(division_result)
