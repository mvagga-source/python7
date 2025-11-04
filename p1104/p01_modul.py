
### 모듈 : 함수의 집합
# 다른 파일의 모듈을 사용하려면 import를 해야 사용가능
# from 파일명(모듈명) import 개별 함수명 (* : 전체), 클래스, 패키지 

# import funcy
# funcy.func2()

# import p1104.cal.funcy as funcy # funcy.cpy의 모든 함수를 가져옴
# print(funcy.func2())

# s1 = funcy.stu() # 클래스 사용

# from math import sin,cos,tan,floor,ceil
# ### floor 소수점 버림, ceil 소수점 올림, round 반올림

# print(floor(1.95))
# print(round(1.59)) # 내장함수

# ### 모듈이름이 길경우 줄여 사용가능 as
# import random as r
# print(r.randint(1,6))

# ### 모듈안의 모든 함수를 출력 dir
# # print(dir(math))
# # print(dir(r))


# # 날짜 - 파이썬, html, 자바스크립트, DB : DB의 날짜 및 시간을 사용한다
# import datetime
# now = datetime.datetime.now()
# print(now)

# import time
# print("a")
# time.sleep(5)
# print("a")


# 패키지
# 모듈파일을 모아둔 폴더
# 폴더명.모듈명 import 변수, 함수, 클래스, *
from cal.funcy import *
print(func1())
