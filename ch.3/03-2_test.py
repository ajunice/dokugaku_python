# 확인문제 1

x = 2
y = 10
if x > 4:
    if y > 2:
        print(x * y)
else:
    print(x + y)
print()

x = 1
y = 4
if x > 4:
    if y > 2:
        print(x * y)
else:
    print(x + y)
print()

x = 10
y = 2
if x > 4:
    if y > 2:
        print(x * y)
else:
    print(x + y)
print()
# 얘는 출력이 없다. 

# 2번
number = input("정수 입력> ")
x = int(number)
if x > 10 and x < 20:
    print("조건에 맞습니다.")
print()

# 3번
str_input = input("태어난 해를 입력해주세요> ")
birth_year = int(str_input) % 12

if birth_year == 0:
    print("원숭이 띠입니다.")
elif birth_year == 1:
    print("닭 띠입니다.")
elif birth_year == 2:
    print("개 띠입니다.")
elif birth_year == 3:
    print("돼지 띠입니다.")
elif birth_year == 4:
    print("쥐 띠입니다.")
elif birth_year == 5:
    print("소 띠입니다.")
elif birth_year == 6:
    print("범 띠입니다.")
elif birth_year == 7:
    print("토끼 띠입니다.")
elif birth_year == 8:
    print("용 띠입니다.")
elif birth_year == 9:
    print("뱀 띠입니다.")
elif birth_year == 10:
    print("말 띠입니다.")
elif birth_year == 11:
    print("양 띠입니다.")

