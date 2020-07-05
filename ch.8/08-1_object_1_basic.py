# 학생 리스트를 선언
students = [
    { "name": "이윤지", "korean": 87, "math": 98, "english": 88, "science": 95 },
    { "name": "윤나리", "korean": 92, "math": 98, "english": 96, "science": 98 },
    { "name": "김지은", "korean": 76, "math": 96, "english": 94, "science": 90 },
    { "name": "정지수", "korean": 98, "math": 92, "english": 96, "science": 92 },
    { "name": "하민희", "korean": 95, "math": 98, "english": 98, "science": 98 },
    { "name": "이상복", "korean": 64, "math": 88, "english": 92, "science": 92 }
]

# 학생을 한 명씩 반복
print("이름", "총점", "평균", sep="\t")
for student in students:
    # 점수의 총합과 평균
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_average = score_sum / 4
    # 출력
    print(student["name"], score_sum, score_average, sep="\t")
