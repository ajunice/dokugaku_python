# 왼쪽 정렬 삼각형
print("1. 왼쪽 정렬 삼각형")
print(">>입력한 숫자만큼 출력되는 삼각형")
n=int(input("줄 수를 입력하세요: "))
for i in range(1, n+1): # range() 함수에서 끝 값은 포함이 안 됨. 따라서 범위를 n+1까지로
    for y in range(i): # 줄 수와 별 수가 같이 늘어남. 별을 i만큼 출력
        print("*", end="")
    print()
    
print(">>무조건 5줄만 생기는 삼각형")
for n in range(5):
  print("*" * (n+1))    


