

# def s_print(str1, num):
#     for i in range(num):
#         print(str1)

# str1 = input("글자를 입력 : ")
# num = int(input("반복횟수를 입력 : "))
# s_print(str1, num)

### 사칙연산을 받아 계산한값을 출력
# def cal(num1,num2,str1):
#     if str1 == "+":
#         print(f"{num1} + {num2} = {num1+num2}")
#     elif str1 == "-":
#         print(f"{num1} - {num2} = {num1-num2}")
#     elif str1 == "*":
#         print(f"{num1} * {num2} = {num1*num2}")
#     elif str1 == "/":
#         print(f"{num1} / {num2} = {num1/num2}")
    
# num1 = int(input("숫자를 입력 : "))
# num2 = int(input("숫자를 입력 : "))

# str1 = input("원하는 사칙연산 기호를 입력 (+,-,*,/) : ")

# cal(num1,num2,str1)


def cal(num1,num2):
    sum = 0
    for i in range(num1,num2+1):
        sum += i
    print("합계 :",sum)

num1 = int(input("숫자를 입력 : "))
num2 = int(input("숫자를 입력 : "))

cal(num1, num2)











