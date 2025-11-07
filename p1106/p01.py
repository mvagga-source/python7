
from stuClass import *
from stusClass import *

stu = StuClass()
stus = StusClass()
        
while True:    

    stu.menu_f()
    select_m = int(input("학생성적매뉴 선택 >> "))
    
    if select_m == 1:
        stu.input_f()
    elif select_m == 2:
        stus.print_f(stu)
    elif select_m == 3:
        pass
    elif select_m == 4:
        pass
    elif select_m == 5:
        pass
    elif select_m == 0:
        print("프로그램 종료!!")
        break



