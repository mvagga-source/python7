
print("-"*50)

# for i in range(2,10):
    
#     if i%2 != 0:
#         continue
    
#     print("[ {} 단 ]".format(i))
#     for j in range(1,10):
#         # print(i,"*",j,"=",i*j)
#         print("{} * {} = {}".format(i,j,i*j),end = "\t")
#     print() # \n


### 중첩 for문을 사용해서 00,01,02,03
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             print("번호표 : {}{}{}".format(i,j,k),end = "\t")
#         print()


### 501 ~ 1000까지 홀수의 합을 출력

sum = 0
# for i in range(501,1001):
#     if i%2 == 1:
#         sum = sum + i
#         print("{} 홀수의 합 : {:,}".format(i, sum))
# print("홀수의 합 : {:,}".format(sum))

# ### 1~100까지 3의 배수의 합을 출력

# sum = 0
# for i in range(1,101):
#     if i%3 == 0:
#         sum = sum + i
#         print("{} 3의 배수의 합 : {:,}".format(i, sum))
# print("3의 배수의 합 : {:,}".format(sum))


fruits = ['사과','배','복숭아','딸기','포도']

### enumerate

for i,fruit in enumerate(fruits):
    print("{}.{}".format(i+1,fruit), end="\t")
print()
    
for i in range(len(fruits)):
    print("{}.{}".format(i+1,fruits[i]), end="\t")
print()





print("-"*50)