
import random

### 변수 선언

a_ok = []
count = 0

# 1~45까지 6개의 랜덤숫자를 출력
# 중복은 안됨

a_list = random.sample(range(1,45),6)
a_list.sort()
print(a_list)    

# 6개의 숫자를 입력받아 출력

a_lists = []
for _ in range(6):
    num = int(input("숫자 입력 : "))
    a_lists.append(num)
a_lists.sort()

#---------------------------
print("*"*50)    
print(a_lists)

for i in a_list:
    for j in a_lists:
        if i == j:
            a_ok.append(i)
            count += 1
            break
            

###  결과화면 출력----------------------------

print("정답갯수 : ",count)
print(a_ok)

# 2개 - 5천원, 3개 - 5만원, 4개 - 1백만원, 5개 - 5천만원, 6개 - 20억

### 당첨금 출력

if count<2:
    val = "0원"
elif count==2:
    val = "5천원"
elif count==3:
    val = "5만원"
elif count==4:
    val = "1백만원"
elif count==5:
    val = "5천만원"
else:
    val = "20억원"
print("당첨금 : "+val)
