
print("-"*50)

# while True: #무한루프

# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)


# i = 1
# sum = 0
# while i<11:
#     sum = sum + i
#     i = i + 1        
# print(sum)


### 5번 동안 숫자를 입력받아 합계를 출력

# sum = 0
# for _ in range(5):
#     num = int(input("숫자를 입력 : "))
#     sum += num
# print(sum)

# sum = 0
# i = 0
# while i<5:
#     num = int(input("숫자를 입력 : "))
#     sum += num
#     i += 1
# print(sum)    

stu_list = []

while True:
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*20)
    
    no = int(input("원하는 번호를 입력 : "))
    if no == 0: break
    elif no == 1:
        
        print("[학생성적입력]")
        
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
        stu_list = [name,kor,eng,math,total,avg]

        print("이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(\
            *stu_list))
        
    elif no == 3:
        
        stu_list = [
            ["홍길동",100,90,80,270,80.00],
            ["김길동",90,90,89,269,90.00],
            ["이길동",100,100,100,300,80.00]
        ]
        
        while True:

            print("[학생성적 수정]")
            print("0. 홍길동")
            print("1. 김길동")
            print("2. 이길동")
            print("-"*50)

            num = int(input("수정하려는 학생번호를 입력하세요>>> "))
            print("[ {} 학생 선택 ]".format(stu_list[num][0]))
            print("1. 국어성적 수정")
            print("2. 영어성적 수정")
            print("3. 수학성적 수정")
            print("-"*50)

            subject = int(input("수정하려는 과목을 선택하세요>>> "))

            print("[ {} 학생 {} 점수 수정 ]".format(stu_list[num][0], titles[subject]))
            print("현재 {} 점수 : {}".format(titles[subject], stu_list[num][subject]))
            score = int(input("수정하려는 {} 점수를 입력하세요>>> ".format(titles[subject])))
            
            # 국어점수 수정
            stu_list[num][subject] = score 
            # 합계 수정
            stu_list[num][4] = stu_list[num][1]+stu_list[num][2]+stu_list[num][3] 
            # 평균 수정
            stu_list[num][5] = stu_list[num][4]/3 

            print(stu_list)






### 구구단
# i = 2
# while i<10:
    
#     print(f"{i}단 //", end="\t")
#     j = 1
#     while j<10:
        
#         print(f"{i} * {j} = {i*j}",end="\t")

#         j = j + 1
#     print()
    
#     i = i + 1    
    
