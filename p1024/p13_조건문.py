
# if문은 : 으로 닫아줘야 함
# 아래 문구는 들여쓰기를 해야 함


# if 10>5:
#     print("정상")
# else:
#     print("비정상")


# 숫자를 입력받아 100보다 큰수인지 아닌지 출력
# 100보다 큰수 입니다. 100보다 작은수 입니다.

print("-"*30)

# num = int(input("숫자를 입력 : "))

# if num > 100:
#     print("100보다 큰수 입니다")
# else:
#     print("100보다 작은수 입니다")

# if num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")
    
    
# 내부모듈    
import datetime

now = datetime.datetime.now()
# print(now)
# print(now.year,"년도")
# print(now.month,"월")
# print(now.day,"일")
# print(now.hour,"시")
# print(now.minute,"분")
# print(now.second,"초")
    
# jumin = input("주민번호를 입력 : ")
jumin = "990201-2111111"

# print(int(jumin[2:4]), now.month)

if int(jumin[2:4]) == now.month:
    print("이벤트 대상 입니다!")
else:
    print("이벤트 대상이 아닙니다!")





    
    
print("-"*30)