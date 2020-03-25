pi = 3.14159265
print(pi)
print(pi+2)
print(pi-2)
print(pi*2)
print(pi/2)
print(pi%2)
print(pi*pi)

#복합 대입 연산자
print()
number = 100
number += 10
number += 20
print("number:", number)

print()
string = "안녕하세요"
string += "!"
string += "!"
print("string:", string)

#사용자 입력: input()
print()
input("인사말을 입력하세요>")
string = input("인사말을 입력하세요>")
print(string) 

#input() 함수의 입력 자료형 
print()
print(type(string)) # > 옆에 안녕하세요 등의 글자를 입력하면 <class 'str'>이 뜬다

number = input("숫자를 입력하세요>")
print(number)
print(type(number))

print()
print("#확인 문제 4")
str_input=input("숫자 입력>")
num_input=float(str_input)
print()
print(num_input, "inch")
print((num_input * 2.54), "cm")
print("#확인 문제 5")
str_input = input("원의 반지름 입력>")
num_input = float(str_input)
print()
print("반지름:", num_input)
print("둘레:", 2*3.14*num_input)
print("넓이:", 3.14*num_input**2)
print("#확인 문제 6")
a = input("문자열 입력>")
b = input("문자열 입력>")
print(a,b)
print(b,a)
print(a,b)
c=a
a=b
b=c
print(a,b)
