
a_list = [1,2,3,4,5]
b_list = list(range(1,6))
c_list = [i for i in range(1,5)] # 리스트 내포

# print(a_list)
# print(b_list)
# print(c_list)

# 입력 : append, insert, extend
# 삭제 : pop, del, remove, clear
# 수정 : a_list[index] = 값
# index : 해당 위치값 리턴

aa_list = [10,5,15,7,9]
print(aa_list.index(10))

### 비교
# print(aa_list)
# num = int(input("원하는 번호를 입력하세요 >> "))
# for idx, aa in enumerate(aa_list):
#     if aa == num:
#         aa_list[idx] = "X"
# print(aa_list)

# print(aa_list)
# num = int(input("원하는 번호를 입력하세요 >> "))

# if num in aa_list:
#     aa_list[aa_list.index(num)] = "X"

# print(aa_list)

###  5*5의 2차원 형태 리스트 생성
# 좌표만들기

import random

a_list = list(range(1,26))
random.shuffle(a_list)
print(a_list)

while True:
    print("-"*50)
    for idx, val in enumerate(a_list):
        print(val,end="\t")
        if (idx+1)%5 == 0:
            print()
    print("-"*50)
    
    num = int(input("원하는 번호를 입력 >>> "))
    
    if num in a_list:
        a_list[a_list.index(num)] = "X"



