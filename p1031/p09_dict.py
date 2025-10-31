
a_list = [1,1,2,3,4,2,3,1,5,4]
a_dic = {}

# 1: 2:
# 딕셔너리에 저장

for i in a_list:
    if i in a_dic:
        a_dic[i] += 1
    else:
        a_dic[i] = 1
        
print(a_dic)

# b_dic = {}
# # 딕셔너리 추가 (없는 키 입력시)
# b_dic["홍길동"] = 100
# # 딕셔너리 수정 (있는 키 입력시)
# b_dic["홍길동"] = 50
