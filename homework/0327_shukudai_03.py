# 가운데 정렬 삼각형
print("3. 가운데 정렬 삼각형")
print(">>입력한 숫자만큼 출력되는 삼각형")
n=int(input("줄 수를 입력하세요."))
for i in range(1, n+1):
    for j in range(n+1-i): # (전체 줄 수-i)만큼 공백 출력
        print(" ", end="")
    for j in range(2*i-1): # (현재 줄 수x2-2)만큼 공백 출력 
        print("*", end="")
    print()

print(">>무조건 5줄만 생기는 삼각형")
for n in range(5):
  print("{:^10}".format("*"*(n+(n+1)))) #{:^10} 가운데 정렬


