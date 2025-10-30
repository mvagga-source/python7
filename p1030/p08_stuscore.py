
import random

stu_list = [
    [10101,"홍길동",80,80,80,240,80.00],
    [10102,"김길동",90,90,90,270,90.00],
    [10103,"이길동",100,100,100,300,100.00]
]

# stu_list = []

stu_count = 10104   # 학생번호

titles = ['번호','이름','국어','영어','수학','합계','평균']


# 학생성적 프로그램

while True:
    print("-"*50)
    print(""*10,"[ 학생성적 프로그램 ]")
    print("-"*50)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("0. 학생성적 종료")
    print("-"*50)
    choice = int(input("원하는 번호를 입력 >> "))
    print()
    
    if choice == 1:     # 학생성적 입력
        
        print("/// 학생성적 입력")
        name = input("\t{}번 학생이름을 입력하세요 >> ".format(stu_count))
        kor = int(input("\t국어점수를 입력 >> "))
        eng = int(input("\t영어점수를 입력 >> "))
        math = int(input("\t수학점수를 입력 >> "))
        
        sum = kor+eng+math
        avg = sum/3
        
        stu_list.append([stu_count,name,kor,eng,math,sum,avg])
        stu_count += 1 # 학생번호 증가
        
        print("성적 입력이 완료되었습니다.")
        print()        
        
    elif choice == 2:   # 학생성적 출력
        
        print(""*10,"[ 학생성적 리스트 ]")
        print("-"*50)
        
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        print("-"*50)
        
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stus))

        print()
        
    elif choice == 3:   # 학생성적 수정
        
        print(""*10,"[ 학생성적 수정 ]")
        print("-"*50)        
        
        for idx, stus in enumerate(stu_list):
            print("{}.{} {}".format(idx+1,stus[0],stus[1]))
        print("-"*50)                
        
        num = int(input("수정할 학생의 번호를 입력 >> "))
        flag = int(input("{} {} 학생이 맞습니까? (1.yes, 2.no) >> ".\
            format(stu_list[num-1][0], stu_list[num-1][1])))
        if flag == 2:
            print("수정이 취소 되었습니다.")
            continue
        
        print("[ {} 학생 수정과목 선택 ]".format(stu_list[num-1][1]))
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        print("-"*50)
        subject = int(input("수정하려는 과목을 선택하세요 >> "))
        
        print("현재 {} 점수 : {} ".\
            format(titles[subject+1],stu_list[num-1][subject+1]))
        
        score = int(input("수정하려는 점수를 입력하세요 >> "))
        
        stu_list[num-1][subject+1] = score
        
        # 합계수정
        stu_list[num-1][5] = \
            stu_list[num-1][2]+stu_list[num-1][3]+stu_list[num-1][4]
        # 평균수정
        stu_list[num-1][6] = stu_list[num-1][5]/3
                
        print("{}점수 {}점으로 수정이 완료되었습니다.".\
            format(titles[subject+1],score))
        print()   
    
    
    elif choice == 4:   # 학생성적 삭제
        
        print(""*10,"[ 학생성적 삭제 ]")
        print("-"*50)        
        
        for idx, stus in enumerate(stu_list):
            print("{}.{} {}".format(idx+1,stus[0],stus[1]))
        print("-"*50)                
        
        num = int(input("삭제할 학생의 번호를 입력 >> "))
        flag = int(input("{} {} 학생이 맞습니까? (1.yes, 2.no) >> ".\
            format(stu_list[num-1][0], stu_list[num-1][1])))
        if flag == 2:
            print("삭제가 취소 되었습니다.")
            continue
        
        del stu_list[num-1]
                
        print("삭제 완료되었습니다.")
        print()                
        
    elif choice == 0:   # 학생성적 종료
        print("[ 프로그램을 종료 합니다 ]")
        print()
        break
        