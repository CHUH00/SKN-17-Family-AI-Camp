import random

teacher_name = '다람쥐'
student_count = 29

def study():
    print(f"{ student_count }명의 학생들이 열심히 공부를 한다!!!")

def lecture():
    print(f"{ teacher_name } 선생님이 수업 중이다~~~~~")

def go_lunch(menus):
    # choice_menu = random.choice(menus)
    return random.choice(menus)
