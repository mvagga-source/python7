
import random

# 4*4 리스트 출력

a_list = list(range(1,10))
print(a_list)


### 랜덤섞기
random.shuffle(a_list)


while True: # 무한반복
    
    print("[좌표 맞추기 게임]")
    print("-"*30)
    print(a_list)
    for idx, a in enumerate(a_list):
        print(a, end = "\t")
        if (idx+1)%3 == 0:
            print()
    print("-"*30)
    
    num = int(input("원하는 번호를 입력하세요.>> "))
    
    # 선택번호가 X표시됨
    for idx, a in enumerate(a_list):
        if a == num:
            a_list[idx] = "X"
            break
        
        
