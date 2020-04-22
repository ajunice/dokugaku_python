# 마름모
print("4. 마름모")
print(">>입력한 숫자만큼 출력되는")
x= int(input("줄 수 홀수로 입력: "))
y= int(x/2)+1            #별이 최대가 되는 가운데 줄(홀수)
for i in range(1,2*y):
    if(i<=y):            
        for j in range(y-i):
            print(" ", end="") #줄 값이 y 이하면 (y - 현재 줄)만큼 공백 출력하고
        for j in range(2*i-1):    
            print("*", end="") #(2 X 현재 줄)-1만큼 별 출력
        print()
    else:
        for j in range(i-y):
            print(" ", end="") #줄 값이 Y보다 크면 (현재 줄-x)만큼 공백 출력하고
        for j in range((2*y-i)*2-1):
            print("*", end="") #(전체 줄-현재 줄)X2-1만큼 별 출력
        print()

print(">>무조건 5줄만 생기는")
for i in range(1, 5, 2):
    print('{:^10}'.format('*' * i))

for i in range(5, 0, -2):
    print('{:^10}'.format('*' * i))

#가운데 정렬 위아래 삼각형을 붙임
for n in range(3):
    print("{:^5}".format("*"*(n+(n+1))))

for n in range(2, 0, -1):
    print("{:^5}".format("*"*((n*2)-1)))

