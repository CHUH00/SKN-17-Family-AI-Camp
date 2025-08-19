# ### 문제 1: **다람쥐의 팀 관리 패키지**

# 다람쥐는 팀 관리를 위해 패키지를 만들어 팀원 정보를 관리하려고 합니다.

# 1. `team_management`라는 패키지를 생성하고, 아래와 같은 모듈을 포함하세요:
#     - `managers.py`: "팀장: 다람쥐" 라는 팀장의 정보를 반환하는 모듈
#     - `developers.py`: "개발자: 산골 다람쥐" 개발자의 정보를 관리하고 반환하는 모듈
# 2. 메인 스크립트에서 이 패키지를 불러와 아래와 같이 출력하세요:
# 팀장: 다람쥐
# 개발자: 산골 다람쥐
    
import team_management_pkg.manage.managers as tm
import team_management_pkg.develop.developers as td

td.developer()
tm.manager()