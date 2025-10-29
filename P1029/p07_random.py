
import random # 선언, random 클래스 가져와서 사용

# print(random.random())  # 0.00000000 <= x < 1.000000000
# print(random.randrange(1,11)) # 1,10사이의 숫자를 랜덤으로 가져옴
# print(random.randint(1,11))   # 1,10사이의 숫자를 랜덤으로 가져옴

# print(random.sample([1,2,3,4,5],4))   # 해당리스트에서 원하는 갯수의 값을 랜덤으로 가져옴 (중복안됨)
# print(random.choices([1,2,3,4,5],k=3))  # 해당리스트에서 원하는 갯수의 값을 랜덤으로 가져옴 (중복가능)

# print(random.choice([1,2,3,4,5]))        # 해당리스트에서 1개를 랜덤으로 가져옴

# 해당리스트 순서를 랜덤으로 조정
# a_list = [1,2,3,4,5]
# random.shuffle(a_list)
# print(a_list)