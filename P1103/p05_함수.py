
# def kor_hello():
#     for i in range(5):
#         print("안녕하세요")

    
# def eng_hello():
#     print("hello")
    
# kor_hello()


def cal(a,b):
    print("[사칙연산]")
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

i = 0
a_list = [0,0]

while True:
    
    num = input("값을 입력 : ")
    if num.isdigit():
        a_list[i] = int(num)
        i = i + 1
    else:
        print("숫자를 입력하시오!!")
        
    if i == 2:
        cal(a_list[0], a_list[1])
        break


    
    