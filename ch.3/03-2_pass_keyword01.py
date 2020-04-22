# pass 키워드를 사용한 미구현 부분 입력
# 입력
number = input("정수 입력> ")
number = int(number)

# 조건문 사용
if number > 0:
    # 양수일 때: 아직 미구현 상태
    pass
else:
    # 음수일 때: 아직 미구현 상태
    pass

# raise NotImplementedError 구문을 넣어 아직 구현하지 않은 부분 알람
# 입력
number = input("정수 입력> ")
number = int(number)

# 조건문 사용
if number > 0:
    # 양수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError
else:
    # 음수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError