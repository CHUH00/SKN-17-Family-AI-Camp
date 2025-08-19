# ### 문제 2: **다람쥐의 업무 관리 패키지**

# 다람쥐는 팀의 업무를 관리하기 위한 패키지를 작성하려고 합니다.

# 1. `work_management`라는 패키지를 생성하고, 아래와 같은 모듈을 포함하세요:
#     - `task_tracking.py`: 작업 상태를 관리하는 모듈
#     함수 start_task(task):"작업 '{task}' 시작됨." 반환
# 함수 end_task(task): "작업 '{task}' 종료됨." 반환
# reporting.py: 업무 보고를 관리하는 모듈
# 함수 generate_report(task): "'{task}' 작업 보고서 생성됨." 반환

# 2. 메인 스크립트에서 이 패키지를 불러와 아래와 같이 출력하세요:
# 작업 '코드 리뷰' 시작됨.
# 작업 '코드 리뷰' 종료됨.
# '코드 리뷰' 작업 보고서 생성됨.

import work_management.task_tracking as wt
import work_management.reporting as wr

task = '코드 리뷰'
wt.start_task(task)
wt.end_task(task)
wr.generate_report(task)