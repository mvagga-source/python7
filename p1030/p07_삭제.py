
stu_list = [
    ["홍길동",80,80,80,240,80.00],
    ["김길동",90,90,90,270,90.00],
    ["이길동",100,100,100,300,100.00]
]

titles = ['이름','국어','영어','수학','합계','평균']

# for stus in stu_list:
#     print("{}\t{}".format(stus[0], stus[1]))
#     print("{}\t{}".format(*stus))
    
# for idx, val in enumerate(stu_list):
#     print("{}.{}".format(idx+1,val[0]))
#     print("{}.{}".format(idx+1,*val))

while True:
    print("[ 학생성적 삭제 리스트 ]")
    for idx, val in enumerate(stu_list):
        print("{}.{}".format(idx+1,val[0]))
    print("-"*50)
    num = int(input("삭제하려는 번호를 입력>> "))
    del stu_list[num-1]
    print(stu_list)