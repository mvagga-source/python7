
### 학생성적입력, 출력, 수정, 삭제를 구현

# stu_list = []
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00],
    [10102,'유관순',90,90,90,280,90.00],
    [10103,'이순신',100,100,100,300,100.00]
]

#학생번호
stu_count = 10104  

titles = ['번호','이름','국어','영어','수학','합계','평균']

while True:
    
    print("="*50)
    print("[ 학생성적관리 프로그램 ]")
    print("="*50)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("5. 종료")
    print("="*50)
    print()
    
    num = int(input("원하는 번호를 선택하세요 >> "))
    
    if num == 1:
        
        print("[학생성적 입력]")
        print("-"*30)
        
        name = input("학생 이름을 입력 : ")
        kor = int(input("국어 점수를 입력 : "))
        eng = int(input("국어 점수를 입력 : "))
        math = int(input("국어 점수를 입력 : "))
        total = kor+eng+math
        avg = total/3
        
        stu_list.append([stu_count,name,kor,eng,math,total,avg])
        stu_count += 1
        
        print()
        print(">> 학생성적 입력 완료!")
        print()        
        
    elif num == 2:
        
        print("[학생성적 출력]")
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        print("-"*50)
        for stu in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stu))
        print("-"*50)
        print()
        
    elif num == 3:
        
        print("[학생성적 수정]")
        print("-"*50)
        for idx, stu in enumerate(stu_list):
            print("{}.{}".format(idx+1, stu[1]))
        print("-"*50)
        num = int(input("수정을 원하는 학생을 선택 >> "))
        print()
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        subject = int(input("{} 학생의 과목을 선택 >> ".format(stu_list[num-1][1])))
        print("{} 학생의 현재 {} 점수 : {}".format(\
            stu_list[num-1][1], titles[subject+1], stu_list[num-1][subject+1]))
        
        scount = int(input("수정을 원하는 {} 점수를 입력 : ".format(titles[subject+1])))
        
        stu_list[num-1][subject+1] = scount
        
        # 합계        
        stu_list[num-1][5] = stu_list[num-1][2]+stu_list[num-1][3]+stu_list[num-1][4]
        
        # 평균
        stu_list[num-1][6] = stu_list[num-1][5]/3
        
        print()
        print(">> 학생성적 수정 완료!")
        print()        
        
    elif num == 4:

        print("[학생성적 삭제]")
        print("-"*50)
        for idx, stu in enumerate(stu_list):
            print("{}.{}".format(idx+1, stu[1]))
        print("-"*50)
        num = int(input("삭제를 원하는 학생을 선택 >> "))
        print()
        
        numyn = int(input("정말로 {} 성적 삭제를 원하십니까? ( 1.yes, 2.no ) ".format(stu_list[num-1][1])))
        print()
        
        if numyn == 2:
            print(">> 삭제가 취소되었습니다!")            
            continue
        
        del stu_list[num-1]        
        
        print()
        print(">> 학생성적 삭제 완료!")
        print()        

    else:
        print("[학생성적관리 프로그램 종료!]")
        break
    