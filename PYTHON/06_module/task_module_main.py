# 다람쥐는 팀에서 업무 진행 상황을 기록하는 프로그램을 작성하려 합니다. `task_module.py`를 생성하고 이를 사용해 아래 요구사항을 구현하세요.

# 1. **`task_module.py` 내용**:
#     - 함수 `start_task(task_name)`: "작업 '{task_name}'이(가) 시작되었습니다." 반환
#     - 함수 `complete_task(task_name)`: "작업 '{task_name}'이(가) 완료되었습니다." 반환
# 2. 메인 스크립트에서 `task_module.py`를 불러와 아래와 같이 출력하세요:
#     "작업 '코드 리뷰'이(가) 시작되었습니다."
# "작업 '코드 리뷰'이(가) 완료되었습니다."

import task_module as tm

tm.start_task('코드 리뷰')
tm.complete_task('코드 리뷰')