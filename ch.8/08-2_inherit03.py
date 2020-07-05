class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("##### 내가 만든 오류가 생성됐다! #####")
    def __str__(self):
        return "오류가 발생했다.."

raise CustomException
