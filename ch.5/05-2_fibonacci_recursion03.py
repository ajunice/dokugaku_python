# 재귀 함수로 구현한 피보나치 수열(3)
# 변수 선언
counter = 0

# 함수 선언
def fibonacci(n):
    counter += 1
    # 피보나치 수를 구한다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 함수 호출
print(fibonacci(10))
# 예외가 출력될 것
# [global 변수 이름]으로 코드 수정해야 함