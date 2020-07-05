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

    def __str__(self, student):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(student),
            self.get_average(student))

    def __eq__(self, value): 
        return self.get_sum() == value.get_sum()
    def __ne__(self, value): 
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le____(self, value):
        return self.get_sum() <= value.get_sum()

# 학생 리스트 선언
students = [
    Student("이윤지", 87, 98, 88, 95),
    Student("하민희", 92, 98, 96, 98),
    Student("윤나리", 76, 96, 94, 90),
    Student("이상복", 98, 92, 96, 92),
    Student("정지수", 95, 98, 98, 98),
    Student("김지은", 64, 88, 92, 92)
]

# 학생 선언
student_a = Student("이윤지", 87, 98, 88, 95),
student_b = Student("하민희", 92, 98, 96, 98),

# 출력
print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a >  student_b = ", student_a >  student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a <  student_b = ", student_a <  student_b)
print("student_a <= student_b = ", student_a <= student_b)
