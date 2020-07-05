# 딕셔너리를 리턴하는 함수 선언
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

# 학생을 처리하는 함수 선언
def student_get_sum(student):
    return student["korean"] + student["math"] +\
        student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student))

# 학생 리스트를 선언
students = [
    create_student("이윤지", 87, 98, 88, 95),
    create_student("윤나리", 92, 98, 96, 98),
    create_student("김지은", 76, 96, 94, 90),
    create_student("정지수", 98, 92, 96, 92),
    create_student("하민희", 95, 98, 98, 98),
    create_student("이상복", 64, 88, 92, 92)
]

# 학생을 한 명씩 반복
print("이름", "총점", "평균", sep="\t")
for student in students:
    # 출력
    print(student_to_string(student))
