
# # stu_list = [name:"홍길동",kor:100,eng:100,math:100]
# # stu_list = {키:값,키:값,키:값...} # 쌍 2개가 하나로 묶인 자료구조

# # 딕셔너리 생성
# list1 = [1,2,3]
# dic1 = {1:'a',2:'b',3:'c'}
# dic2 = {"no":1,"name":"홍길동","class":3}

# print(dic1)

# # 딕셔너리 추가
# stu = {"학번":1,"이름":"홍길동","학과":"컴퓨터공학"}
# print(stu)
# stu['연락처'] = "010-1111-1111"
# print(stu)

# # 딕셔너리 수정
# stu['이름'] = "고길동"
# print(stu)

# # 딕셔너리 삭제
# del(stu["이름"])
# print(stu)


stu_list = [
    {"no":1,"name":"홍길동","kor":100}
]

print(stu_list[0]["no"])
print(stu_list[0]["name"])

a_dic = {"no":1,"name":"홍길동","kor":100}

print(a_dic["kor"])     # 없는 키값 입력 시 에러
print(a_dic.get("kor")) # 없는 키값 입력 시 none출력

# 딕셔너리 keys()
print(a_dic.keys()) # key값만 가져오기
a_list = list(a_dic.keys()) # list로 형변환 필요
print(a_list)

# 딕셔너리 values()
print(a_dic.values())
b_list = list(a_dic.values())
print(b_list)

# 딕셔너리 items() - key, value
print(a_dic.items()) # 튜플형식임
c_list = list(a_dic.items())
print(c_list)
print(c_list[1][1])

# 딕셔너리 키 존재 여부
stu_dic = {"no":1,"name":"홍길동","kor":100}
if "kor" in stu_dic:
    print("키 존재")
else:
    print("키 존재 안함")










