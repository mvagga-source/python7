print("-"*30)


### 1~5 for문을 사용해서 출력

# for i in range(5):
#     print(i+1)


### 숫자를 입력받아 입력받은 값을 출력 하는것을 5번 반복

# for i in range(5):
#     print(int(input("숫자 {} 입력 :".format(i+1))))


### 1~10 까지 숫자의 합을 출력

# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print("합계 :",sum)

### 1~10까지 홀수 합계

sum = 0
for i in range(1,11,2):
    sum = sum + i
print("합계 :",sum)


sum = 0
for i in range(1,11):
    if i%2 != 0: # 또는 if i%2 == 1:
        sum = sum + i
print("합계 :",sum)














# for i in range(10):
#     print("반갑")
    

# 중첩 - if, for .. 등을 2번이상 사용

# a_list = []
# sum = 0
# for i in range(10):
#     num = int(input("숫자를 입력 : "))
#     if num%2 == 0:
#         break
#     a_list.append(num)
#     sum = sum + num

# print("리스트 : {}, 합계 : {}".format(a_list, sum))











print("-"*30)