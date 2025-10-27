
# 리스트, 튜플, 세트
# 리스트 - 배열 : 데이터를 여러개 저장하는 공간 / 복합 타입 정의 가능


print("-"*30)

# stuscore = ['홍길동',100,100]
# print(stuscore)

# # 추가
# stuscore.append(99)
# print(stuscore)

# # (n, v) n번째 위치에 v값을 입력
# stuscore.insert(1, 5)
# print(stuscore)

# # 맨뒤 삭제
# stuscore.pop()
# print(stuscore)

# # 해당 리스트값 삭제
# stuscore.remove("홍길동")
# print(stuscore)
# stuscore.remove(100)
# print(stuscore)


fruit = ["사과","배","수박","딸기","포도"]
# input1 = input("좋아하는 과일 입력 : ")
# fruit.append(input1)
# print("입력과일종류 :", fruit)

# 해당하는 과일을 삭제
# input1 = input("좋아하는 과일 입력 : ")
# print("리스트 과일종류 :", fruit)
# if input1 in fruit:
#     fruit.remove(input1)
# else:
#     print("해당되는 과일이 없음")
# print("입력 과일종류 :", fruit)



# 1개의 글자를 입력받아 변수에 존재하는지 확인
# str1 = "안녕하세요. 반갑습니다. 저는 홍길동 입니다."

# input1 = input("1개의 글자를 입력 : ")

# if input1 in str1:
#     print("[%s] 글자 존재" % input1)
# else:
#     print("[%s] 글자 존재하지 않음" % input1)



stu_data = [] # 리스트
stu_data.append(1)
stu_data.append("홍길동")
stu_data.append(100)
stu_data.append(100)
stu_data.append(100)
print(stu_data)

stu_datas = []
stu_datas.append(stu_data)

stu_datas[
    [1, '홍길동', 100],
    [1, '홍길동', 100]
]








print("-"*30)