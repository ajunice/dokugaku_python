# 2번
# 숫자는 무작위로 입력해도 상관 없다.
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(0, len(key_list)):
    character[key_list[i]] = value_list[i]

# 최종 출력
print(character)

# 3번
limit = 10000
i = 1

# sum은 이미 파이썬 내부에서 사용하고 있는
# 식별자이므로 sum_value라는 변수 이름을 사용했다.
sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))

# 4번
max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - i
  
    # 최댓값 구하기
    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))
