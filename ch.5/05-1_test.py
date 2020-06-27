# 1-1번
def f(x):
    return 2 * x + 1
print(f(10))

# 1-2번
def f(x):
    return x ** 2 + 2 * x + 1
print(f(10))

#2번
def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output

# 함수 호출
print(mul(5, 7, 9, 10))

