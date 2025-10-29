
import random

r_list = []
r_num = random.randrange(1,101)
for _ in range(5):
    my_num = int(input("숫자 입력 : "))
    r_list.append(my_num)
    if my_num == r_num:
        print("당첨!")
        break
    elif r_num>my_num:
        print("더 큰수 입력!")
    else:
        print("더 작은수 입력!")
        
print("당첨번호 : ",r_num)        

print("입력번호 : ",end=" ")
for i in range(len(r_list)):
    print(f"{r_list[i]}",end=" ")

# randrange() 1~10까지의 랜덤숫자를 3개 출력

# for _ in range(3):
#     print(random.randrange(1,11))
    
# print(random.sample([1,2,3,4,5,6,7,8,9],5))
# print(random.sample(range(1,11),5))
    