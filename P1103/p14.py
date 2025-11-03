
# 로또 맞추기 프로그램
# 로또3개를 자동번호 추출받아 몇개가 맞는지 출력

import random

r_list = [] # 로또값
my_list = [] # 내가 입력한 값
c_list = [0,0,0] # 결과값

for i in range(3):
    r_list.append(random.sample(range(1,46),6))

print(r_list)

# 번호비교

while len(my_list) < 3:
    
    num = input("(1~45) 번호를 입력>> ")
    if not num.isdigit():
        print("숫자만 입력 가능!!")
        continue
    
    num = int(num)
    
    if num > 45 or num < 1:
        print("1~45 값만 입력 가능!!")
        continue
    
    my_list.append(num)
    
i = 0
for r in r_list:
    for m in my_list:
        if m in r:
            c_list[i] += 1
    i += 1
        
print(c_list)

