
import random
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00],
    [10102,'유관순',90,90,90,280,90.00],
    [10103,'이순신',100,100,100,300,100.00]
]
stu_count = 10104  #학생번호
titles = ['번호','이름','국어','영어','수학','합계','평균']

# 학생입력부분


# 학생출력부분
while True:
    print("-"*50)
    print(" "*10,"[ 학생성적프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print("-"*50)
    
    msel = int(input("학생성적프로그램 선택 >> "))
    
    if msel == 1:
        
        print("## [학생성적 입력] ## ")
        print("-"*30)
        name = input("이름을 입력 : ")
        kor = int(input("국어점수를 입력 : "))
        eng = int(input("영어점수를 입력 : "))
        math = int(input("수학점수를 입력 : "))
        
        total = kor+eng+math
        avg = total/3
        
        stu_list.append([stu_count,name,kor,eng,math,total,avg])
        stu_count += 1
        print("-"*30)
        print("학생성적 입력 완료!!")        
        print()
        
    elif msel == 2:

        print("## [학생성적 출력] ## ")
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        print("-"*50)
        for stu in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stu))
        print("-"*50)
        print("학생성적 출력 완료!!")        
        print()        

    elif msel == 3:
        
        print("## [학생성적 수정] ## ")
        print("-"*50)        
        for idx, val in enumerate(stu_list):
            print("{}.{}".format)
        
        
        
        
        
    elif msel == 4:
        pass
    else:
        print("[학생성적프로그램 종료 !!]")
        break
    