# 1. **`attendance_module.py` 내용**:
#     - 함수 **`record_attendance(name, time)`**: "{name}님이 {time}에 출근했습니다." 반환
#     - 함수 `record_leave(name, time)`: "{name}님이 {time}에 퇴근했습니다." 반환

def record_attendance(name, time):
    return f"{name}님이 {time}에 출근했습니다."

def record_leave(name, time):
    return f"{name}님이 {time}에 퇴근했습니다."