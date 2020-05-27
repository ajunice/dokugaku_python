# 모래시계 
print("5. 모래시계")
print(">>입력한 숫자만큼 출력되는")


print(">>위에5, 아래 5")
for i in range(9, 0, -2):
    print('{:^10}'.format('*' * i))
    
for i in range(3, 11, 2):
    print('{:^10}'.format('*' * i))
print()

print(">>위아래 다해서 5줄")
for i in range(5, 1, -2):
    print('{:^10}'.format('*' * i))

for i in range(1, 7, 2):
    print('{:^10}'.format('*' * i))
