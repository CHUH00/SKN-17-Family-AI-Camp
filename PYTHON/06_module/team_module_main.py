# ### 문제 1: **다람쥐의 팀원 소개 모듈**

# 다람쥐는 대기업에 입사한 후, 팀원들의 역할을 소개하는 프로그램을 작성하려고 합니다. `team_module.py`라는 모듈을 생성하고 이를 사용해 아래 요구사항을 구현하세요.

# 1. **`team_module.py` 내용**:
#     - 함수 `introduce_manager()`: "저는 팀장입니다. 팀을 이끌고 있습니다." 반환
#     - 함수 `introduce_developer()`: "저는 개발자입니다. LLM 서비스를 개발하고 있습니다." 반환
#     - 변수 `company`: "주식회사 SQUIRREL"
# 2. 메인 스크립트에서 `team_module.py`를 불러와 아래와 같이 출력하세요:
# "안녕하세요, 주식회사 SQUIRREL입니다."
# "저는 팀장입니다. 팀을 이끌고 있습니다."
# "저는 개발자입니다. 프로젝트를 개발하고 있습니다."

import team_module as tm

print("안녕하세요, 주식회사 SQUIRREL입니다.")
tm.introduce_manager()
tm.introduce_developer()