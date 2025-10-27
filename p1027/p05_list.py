
# 과일을 추가하는 프로그램 구현

# fruit = []

# for i in range(3):
#     fruit.append(input("과일 이름을 입력 : "))
#     print("과일리스트 : ", fruit)

# print(fruit)


# names = []

# for i in range(5):

#     name = input("이름을 입력 : ")
#     if name in names:
#         print("이름 중복 : ", name)
#     else:
#         names.append(name)
#         print(names)
        
    
    
stus_data = []

for i in range(3):

    stu_data = []

    name = input("이름을 입력 : ")
    kor = input("국어 점수 입력 : ")
    eng = input("영어 점수 입력 : ")
    math = input("수학 점수 입력 : ")

    total = int(kor)+int(eng)+int(math)
    avg = total/3

    stu_data.append(name)
    stu_data.append(kor)
    stu_data.append(eng)
    stu_data.append(math)
    stu_data.append(total)
    stu_data.append(avg)

    stus_data.append(stu_data)
    
    
print(stus_data)