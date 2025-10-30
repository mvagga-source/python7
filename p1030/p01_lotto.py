
# 로또 맞추기 프로그램을 구현

# 1.변수선언

import random

lot_list = []
my_list = []
re_list = []

# 2. 6개 번호생성

# print(list(range(1,46)))
lot_list = random.sample(range(1,46),6)
lot_list.sort()
print(f"로또번호 : {lot_list}")
print("-"*50)

# 3. 6개 번호입력

while len(my_list) < 6:
    
    num = input(f"1 ~ 45 숫자를 입력하세요 ({len(my_list)}개 선택됨) : ")
    
    if not num.isdigit():
        print("숫자만 입력 가능 합니다.")
        continue

    num = int(num)
    
    if num in my_list: # 존재 여부 확인
        print("중복 입력 입니다.")
        continue
    
    if 1<= num <= 45:
        my_list.append(num)
    else:
        print("잘못된 번호를 입력하셨습니다.")
    
print(f"입력한 번호 : {my_list}")
print("-"*50)

# 4. 번호확인

# for i in lot_list:
#     for j in my_list:
#          j in i:
#             re_list.append(i)
#             break

for i in lot_list:
    if i in my_list: # 존재 여부 확인
       re_list.append(i)

# 5. 결과출력

ok_cnt = len(re_list)

re_value = "당첨금액 : "

if ok_cnt < 2:
    re_value += "0원"
elif ok_cnt == 2:
    re_value += "5,000원"
elif ok_cnt == 3:
    re_value += "50,000원"
elif ok_cnt == 4:
    re_value += "1,000,000원"
elif ok_cnt == 5:
    re_value += "1,000,000,000원"
elif ok_cnt == 6:
    re_value += "20,000,000,000원"

print(f"맞춘 갯수 : {len(re_list)}")
print(f"맞춘 번호 : {re_list}")
print("-"*50)
print(f"{re_value}")
print("-"*50)



