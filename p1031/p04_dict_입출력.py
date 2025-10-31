
#stu_dic = {"no":1,"name":"홍길동","kor":100}

# stu_dic = {}
# print(stu_dic)

# stu_dic["no"] = 1
# stu_dic["name"] = "홍길동"
# stu_dic["kor"] = 100
# print(stu_dic)


# for k,v in stu_dic.items():
#     print("{}:{}".format(k,v))
    
# for k in stu_dic.keys():
#     print("{}:{}".format(k,stu_dic[k]))
    
# for v in stu_dic.values():
#     print("값 : {}".format(v))


# 다차원 딕셔너리 수정
stu_list = [
    {"no":1,"name":"홍길동","kor":100},
    {"no":2,"name":"유관순","kor":80},
    {"no":3,"name":"이순신","kor":90}
]
print(stu_list)

# 3번째에 있는 kor을 50으로 변경
stu_list[2]["kor"] = 50
print(stu_list)

s_list = {"no":1,"name":"홍길동","kor":100}
s_list["kor"] = 50

a_list = [3,"이순신",90]
a_list[2] = 50

