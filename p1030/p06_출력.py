
stu_list = [
    ["홍길동",80,80,80,240,80.00],
    ["김길동",90,90,90,270,90.00],
    ["이길동",100,100,100,300,100.00]
]

titles = ['이름','국어','영어','수학','합계','평균']

print("-"*50)
print(" "*10,"[ 학생성적 프로그램 ]")
print("-"*50)
print("1. 학생성적 입력")
print("2. 학생성적 출력")
print("-"*50)

choice = int(input("원하는 번호 입력 >>> "))
print()

### 학생성적 출력
print(" "*15,"[ 학생성적리스트 ]")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{}\t".format(*titles))
print("-"*50)

for stus in stu_list:
    print("{}\t{}\t{}\t{}\t{}\t{}\t".format(*stus))