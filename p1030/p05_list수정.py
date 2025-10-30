
# a_list = [1,2,3,4,5,6,7,8,9]
# b_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# # 1차원 리스트 출력
# a_list[3] = 100
# for a in a_list:
#     print(a, end="\t")

# print()    
# print("-"*50)

# # 2차원 리스트 출력

# b_list[1][0] = 100
# b_list[2][1] = 50
# for bs in b_list:
#     for b in bs:
#         print(b, end="\t")
        
        
# stu_list = [
#     ["홍길동",100,90,80,270,80.00],
#     ["김철수",90,90,89,269,90.00],
#     ["이영희",100,100,100,300,80.00]
# ]

# print(stu_list[1][3])
# print(stu_list[2][0])

# ### 

# stu_list[2][2] = 70
# stu_list[2][4] = stu_list[2][1]+stu_list[2][2]+stu_list[2][3]
# stu_list[2][5] = stu_list[2][4]/3

# print(stu_list)

# 0. 홍길동
# 1. 유관순
# 2. 이순신

# 수정하고 싶은 학생번호를 입력
# 국어점수를 변경하는 프로그램

stu_list = [
    ["홍길동",100,90,80,270,80.00],
    ["김길동",90,90,89,269,90.00],
    ["이길동",100,100,100,300,80.00]
]

titles = ['이름','국어','영어','수학','합계','평균']

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


# while True:

#     print("-"*50)            
#     print(stu_list)
#     print()
    
#     print('''\
#         [ 수정할 학생번호 ]
#         0. 홍길동
#         1. 김철수
#         2. 이영희    
#     ''')

#     num = input("수정할 학생번호를 입력하세요>>")
    
#     if not num.isdigit:
#         print("숫자만 입력 가능")
#     else:
#         num = int(num)        
        
#         if num in [0,1,2]:
            
#             stu_list[num][1] = 70
#             stu_list[num][4] = stu_list[num][1]+stu_list[num][2]+stu_list[num][3]
#             stu_list[num][5] = stu_list[num][4]/3    
#         else:
#             print("잘못된 확생 번호 입니다.")
    
        





