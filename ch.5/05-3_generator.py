# 함수 선언
def test():
    print("함수가 호출됐슴니다.")
    yield test

# 함수 호출
print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())
