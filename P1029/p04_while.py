
print("-"*50)

### 테스트
# print("2025",'10','29',sep="")

# 객체 : 파이썬에서 사용되는 모든 자료형



# 이름, 국어 입력받아 출력

stu_list = []

while True:
    print("[ 학생성적입력 ]")

    name = input("이름 입력 ")
    kor = int(input("국어점수 입력 : "))
    eng = int(input("영어점수 입력 : "))
    math = int(input("수학점수 입력 : "))

    total = kor+eng+math
    avg = total/3


    # stu_list.append(name)
    # stu_list.append(kor)
    # stu_list.append(eng)
    # stu_list.append(math)
    # stu_list.append(total)
    # stu_list.append(avg)
    # stu_list = [name,kor,eng,math,total,avg]
    stu_list.append([name,kor,eng,math,total,avg])

    print("이름\t국어\t영어\t수학\t합계\t평균")
    print("-"*50)
    print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(\
        *stu_list))
