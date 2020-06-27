# 파일 오픈
with open("basic.txt", "r") as file:
    # 파일 오픈 앤드 프린트
    contents = file.read()
print(contents)
