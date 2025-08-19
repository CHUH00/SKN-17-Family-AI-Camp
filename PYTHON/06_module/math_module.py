# ### 문제 4: **내장 모듈을 활용한 다람쥐의 업무 효율성 계산**

# 다람쥐는 자신의 업무 효율성을 계산하려고 합니다. `math` 모듈을 사용하여 아래 요구사항을 구현하세요.

# 1. 매일 처리한 업무량을 기록한 배열이 [10, 12, 8, 15, 9]라면 평균 업무량을 출력하세요.
# 2. 평균 업무량보다 많이 처리한 날의 개수를 계산하세요.

import math

record = [10, 12, 8, 15, 9]
s = sum(record)
average = s / len(record)
print(average)

count = 0
for r in record:
    if r > average:
        count += 1
        
print(count)

