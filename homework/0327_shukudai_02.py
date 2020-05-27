# 오른쪽 정렬 삼각형
print("2. 오른쪽 정렬 삼각형")
print(">>입력한 숫자만큼 출력되는 삼각형")
n = int(input("줄 수를 입력하세요:"))
for i in range(1, n+1):
    for j in range(n-i): # (전체 줄 수-i)만큼 공백 출력
        print(" ", end="")
    for j in range(i): # 줄 수만큼 별 출력
        print("*", end="")
    print()

print(">>무조건 5줄만 생기는 삼각형")
for i in range(5):
    print("{:>5}".format("*" * (i +1))) # {:>5} 오른쪽 정렬

#for i in range(5):
#    print("{:<5}".format("*" * (i +1))) # {:<5} 왼쪽 정렬

#for i in range(5):
#    print("{:^5}".format("*" * (i +1))) # {:^5} 가운데 정렬


