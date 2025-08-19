# ### 문제 2: **다람쥐의 출퇴근 관리 모듈**

# 다람쥐는 팀원들의 출퇴근 시간을 관리하는 프로그램을 작성하고자 합니다. `attendance_module.py`를 생성하고 이를 사용해 아래 요구사항을 구현하세요.

# 1. **`attendance_module.py` 내용**:
#     - 함수 `record_attendance(name, time)`: "{name}님이 {time}에 출근했습니다." 반환
#     - 함수 `record_leave(name, time)`: "{name}님이 {time}에 퇴근했습니다." 반환
# 2. 메인 스크립트에서 `attendance_module.py`를 불러와 아래와 같이 출력하세요:
#     "다람쥐님이 9:00에 출근했습니다."
# "다람쥐님이 18:00에 퇴근했습니다."

import attendance_module as am

am.record_attendance('다람쥐', '9:00')
am.record_leave('다람쥐', '18:00')