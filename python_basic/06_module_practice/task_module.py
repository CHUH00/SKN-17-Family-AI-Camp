# 1. **`task_module.py` 내용**:
#     - 함수 `start_task(task_name)`: "작업 '{task_name}'이(가) 시작되었습니다." 반환
#     - 함수 `complete_task(task_name)`: "작업 '{task_name}'이(가) 완료되었습니다." 반환

def start_task(task_name):
    return f"작업 '{task_name}'이(가) 시작되었습니다."

def complete_task(task_name):
    return "작업 '" + task_name + "'이(가) 완료되었습니다."


