
# english = {
#     "사랑":"love",
#     "차":"car",
#     "커피":"coffee",
#     "전화":"phone",
#     "컴퓨터":"computer",
#     "이름":"name",
#     "한국":"korea"
# }

english = {
    "사랑":"love",
    "차":"car",
    "커피":"coffee",
    "전화":"phone",
    "컴퓨터":"computer",
    "이름":"name",
    "한국":"korea"
}

# 영어 맞추기 프로그램을 구현

c = 0
i = 0
a_list = {}

for k,v in english.items():
    
    i += 1
    
    # 정답 입력
    print("{} 은(는) 영어로? ".format(k))

    answer = input(">> ")
    
    # 정답 확인    
    if v == answer:
        print("정답!!")
        c += 1
        a_list[i] = "정답"
    else:
        print("오답!! ",v)
        a_list[i] = "오답"        
        
print("정답 갯수 : ",c) 
print(a_list)   



# names = ['홍','홍','김','이','유','이','홍','김','강','홍']

# n_dic = {}

# for i in names:
#     if i not in n_dic:
#         n_dic[i] = 1
#     else:
#         n_dic[i] += 1
        
# print("n_dic >> ",n_dic)


# a_list = [1,2,3,1,1,2,1,3,4,5]
# a_dic = {}
# # for 변수 in 범위: #범위 - range, list, 문자열, 딕셔너리

# for i in a_list:
#     if i not in a_dic:
#         a_dic[i] = 1
#     else:
#         a_dic[i] += 1
# print("a_dic >> ",a_dic)


# for i in a_list:
#     a_dic[i] = a_list.count(i)
# print("a_dic >> ",a_dic)

# a_dic = {}
# for i in range(len(names)):
#     a_dic[names[i]] = names.count(names[i])
# print("a_dic >> ",a_dic)



# b_dic = {}
# # 1:0, 2:0, 3:0 딕셔너리를 추가
# # 2:5로 변경

# for i in range(1,4):
#     b_dic[i] = 0
# print("b_dic >> ", b_dic)
    
# b_dic[2] = 5
# print("b_dic >> ", b_dic)

# c_dic = {}
# # "홍":100, "이":90, "유":80 딕셔너리 추가
# #"이":95로 변경
# #"유"를 삭제

# c_dic["홍"] = 100
# c_dic["이"] = 90
# c_dic["유"] = 80
# print("c_dic >> ", c_dic)

# c_dic["이"] = 95
# print("c_dic >> ", c_dic)

# del c_dic["유"]
# print("c_dic >> ", c_dic)




# 해당값이 있는지 확인 딕셔너리
# if 7 in a_list:
#     print("존재")
# else:
#     print("없음")
    
# a_dic = {'1':1,'2':3,'3':4}
# if '7' in a_dic: # 키값 체크
#     print("존재")
# else:
#     print("없음")
