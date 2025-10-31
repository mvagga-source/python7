
# 20문제중에 랜덤으로 5문제를 뽑아서 퀴즈를 구현

import random

english = {
    '사랑':'love', '차':'car', '커피':'coffee', '전화':'phone', '컴퓨터':'computer',
    '이름':'name', '한국':'korea', '물':'water', '지구':'earth', '하늘':'sky',
    '공기':'air', '고양이':'cat', '강아지':'dog', '아기':'baby', '엄마':'mother',
    '아빠':'father', '집':'house', '소년':'boy', '소녀':'girl', '열쇠':'key'
}

e_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
quest = random.sample(e_list,6) # 랜덤5개 - 20문제중 5개를 추출
quest.sort() # 랜덤5개 순서대로 정렬
j = 0
c = 0
quest_dic = {}
for i,k in enumerate(english.keys()): # index를 추출
    if i in quest:
        #print(i,k,english[k])
        j += 1
        # 정답 입력
        print("{} 은(는) 영어로? ".format(k))

        answer = input(">> ")
        
        # 정답 확인    
        if answer == english[k]:
            print("정답!!")
            c += 1
            quest_dic[j] = "정답"
        else:
            print("오답!! ",english[k])
            quest_dic[j] = "오답"           
            
print("정답 : ",c)
print(quest_dic)    

# e_list = {}
# e_list = random.sample(list(english.keys()),5)
# print(e_list)

# # # 영어 맞추기 프로그램을 구현

# c = 0
# i = 0
# a_list = {}

# for k in e_list:
    
#     i += 1
    
#     # 정답 입력
#     print("{} 은(는) 영어로? ".format(k))

#     answer = input(">> ")
    
#     # 정답 확인    
#     if answer == english[k]:
#         print("정답!!")
#         c += 1
#         a_list[i] = "정답"
#     else:
#         print("오답!! ",english[k])
#         a_list[i] = "오답"        
        
# print("정답 갯수 : ",c)
# print(a_list)