

import random

# 5*5

# 리스트 생성
a_list = list(range(1,26))

# 리스트 섞기
random.shuffle(a_list)
print(a_list)

# 리스트 화면에 출력

while True:
    print("[ 좌표맞추기 게임 ]")
    print("-"*50)        
    for idx, val in enumerate(a_list):
        print(val,end="\t")
        if (idx+1)%5 == 0:
            print()
    print("-"*50)

    num = int(input("원하는 번호를 입력 >> "))
    print()
    
    # 번호비교
    for idx,a in enumerate(a_list):
        if num == a:
            a_list[idx] = "X"
            break

    # if num in a_list:
    #     a_list.index(num)
