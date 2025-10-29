
print("-"*50)

### 테스트
# print("2025",'10','29',sep="")

# 객체 : 파이썬에서 사용되는 모든 자료형



# 이름, 국어 입력받아 출력

# stu_list = []

# while True:
#     print("[ 학생성적입력 ]")

#     name = input("이름 입력 ")
#     kor = int(input("국어점수 입력 : "))
#     eng = int(input("영어점수 입력 : "))
#     math = int(input("수학점수 입력 : "))

#     total = kor+eng+math
#     avg = total/3

#     stu_list.append([name,kor,eng,math,total,avg])

#     print("이름\t국어\t영어\t수학\t합계\t평균")
#     print("-"*50)
#     print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(\
#         name,kor,eng,math,total,avg))
          
# for i in stu_list:
#     print(stu_list[i])


n_list = []
while len(n_list)<4:
    name = input("{} 번째 이름 입력 : ".format(len(n_list)+1))
    kor = int(input("{} 번째 국어 점수 입력 : ".format(len(n_list)+1)))
    n_list.append([name, kor])
    print(n_list)

print("이름\t국어")
print("-"*50)    
for i in range(len(n_list)):
    print("{}\t{}".format(*n_list[i]))