# import-as, from-import 구문 사용
# 1-1. our_class_pkg 패키지의 official 패키지의 
#       official_module을 om 별칭으로 가져오고 
import our_class_pkg.official.official_module as om
# 1-2. our_class_pkg 패키지의 unofficial 패키지의 
#       unofficial_module을 from-importfh rkwudhktj
from our_class_pkg.unofficial.unofficial_module import study, go_lunch

# 2. 선생님 이름과 학생 수를 출력하고
print(om.teacher_name)
print(om.student_count)

# 3. study() 함수와 lecture() 함수를 호출하고
study()
om.lecture()

# 4. 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
menus = ['짜장', '카레', '탕수육', '깐풍기', '짬뽕']

# 5. go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
print(go_lunch(menus))
