#모두 대문자로
a = "Hello Python Programming...!"
a.upper()
print(a.upper())
#모두 소문자로
a.lower()
print(a.lower())

#문자열 양옆 공백 제거
print("#문자열 양옆 공백 제거")
input_a = """
     안녕하세요
문자열의 함수를 알아봅니다.
"""
print(input_a)
print(input_a.strip())

#문자열 구성 파악하기: isOO( )
print("#문자열 구성 파악하기: isOO( )")
print("TrainA10".isalnum())
print("10".isdigit())

#문자열 찾기: find( )와 rfind( )
print("#왼쪽부터 찾아서 처음 등장하는 위치 찾기: find( )")
output_a = "안녕안녕하세요".find("안녕")
print(output_a)
print("#오른쪽부터 찾아서 처음 등장하는 위치 찾기: rfind( )")
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)

#문자열과 in 연산자 - 문자열 내부에 어떤 문자열이 있는지 확인
print("#문자열과 in 연산자")
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

#문자열 자르기: split( )
print("#문자열 자르기: split( )")
a = "10 20 30 40 50".split(" ")
print(a)
