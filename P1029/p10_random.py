
# 로또번호 맞추기 프로그램

import random

# 1, 변수선언, 로또번호 생성

lo_list = [] # 로또번호
my_list = [] # 내가 입력한 번호
re_list = [] # 맞춘 번호

lo_list = random.sample(range(1,46),6)
lo_list.sort()
print("-"*50)
print(f"로또번호 : {lo_list}")
print("-"*50)

# 2. 숫자입력

for _ in range(6):
    my_num = int(input("숫자 입력 : "))
    my_list.append(my_num)
print(f"입력번호 : {my_list}")

# 3. 당첨번호 확인

for i in my_list:
    for j in lo_list:
        
        if i == j:
            re_list.append(i)
            break

# 4. 결과화면 출력

re_list.sort()

print("-"*50)
print(f"맞춘갯수 : {len(re_list)}")
print(f"맞춘번호 : {re_list}")
print("-"*50)

# 5. 당첨금 출력

if len(re_list)<2:
    imsi = "0원"
elif len(re_list)==2:
    imsi = "5,000원"
elif len(re_list)==3:
    imsi = "50,000원"
elif len(re_list)==4:
    imsi = "1,000,000원"
elif len(re_list)==5:
    imsi = "50,000,000원"
elif len(re_list)==6:
    imsi = "2,000,000,000원"                

print("당첨금 : "+imsi)

print("-"*50)