# 클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()) 

# 학생 리스트 선언
students = [
    Student("이윤지", 87, 98, 88, 95),
    Student("윤나리", 92, 98, 96, 98),
    Student("김지은", 76, 96, 94, 90),
    Student("정지수", 98, 92, 96, 92),
    Student("하민희", 95, 98, 98, 98),
    Student("이상복", 64, 88, 92, 92)
]

# 출력
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))
