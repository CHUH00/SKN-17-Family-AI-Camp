# ### 문제 3: **다람쥐의 개인 일정 관리 패키지**

# 다람쥐는 자신의 일정을 관리하기 위한 패키지를 작성하려고 합니다.

# 1. `schedule_management`라는 패키지를 생성하고, 아래와 같은 모듈을 포함하세요:
#     - `calendar.py`: 다람쥐의 일정을 관리하는 모듈
        
#         ```
#         함수 add_event(event, date):"{date}에 '{event}' 일정이 추가되었습니다." 반환
#         함수 remove_event(event):"'{event}' 일정이 삭제되었습니다." 반환
#         ```
        
# 2. 메인 스크립트에서 이 패키지를 불러와 아래와 같이 출력하세요:
#  2024-01-15에 '회의' 일정이 추가되었습니다.
# '회의' 일정이 삭제되었습니다.

from datetime import datetime
import schedule_management.calendar as sc

date = datetime.now().strftime("%Y-%m-%d")
event = '회의'

sc.add_event(event, date)
sc.remove_event(event)