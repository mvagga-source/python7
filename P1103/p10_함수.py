
def func(*a,b=10):
    print(a)
    print(b)

func(10,1,b=2)


# from stuFunc import * # screen_print, stu_input... => 전체가져오기 : *

# while True:

#     screen_print() # 함수호출
#     choice = int(input("원하는 번호를 입력 >> "))
    
#     if choice == 1:
#         stu_input()
#         stu_print()
#     if choice == 2:
#         stu_print()
#     elif choice == 0:
#         break