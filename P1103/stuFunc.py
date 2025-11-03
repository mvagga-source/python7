
titles = ['번호','이름','국어','영어','수학','합계','평균']

stu_list = [
    [10101,"홍길동",80,80,80,240,80.00],
    [10102,"김길동",90,90,90,270,90.00],
    [10103,"이길동",100,100,100,300,100.00]
]

stu_count = 10104   # 학생번호(지역변수) - 함수를 벗어나면 값이 사라짐

def screen_print():
    
    print("-"*50)
    print(""*10,"[ 학생성적 프로그램 ]")
    print("-"*50)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("0. 학생성적 종료")
    print("-"*50)
    
def stu_input():
    # 단순변수가 선언되면 함수에서는 변수를 새롭게 생성
    global stu_count # 함수 밖에 있는 변수를 가져오기(전역변수)
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

def stu_print():
    
    print(""*10,"[ 학생성적 리스트 ]")
    print("-"*50)
    
    # print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
    print(*titles, sep="\t")
    print("-"*50)
    
    for stus in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stus))

    print()    