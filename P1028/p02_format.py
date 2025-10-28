

print("-"*30)



year = 2025
month = 10
day = 28

# format()함수 / 변수 저장형

# date1 = print("%d년 %d월 %d일" % (year, month, day))
# print(date1)

# date1 = "{}년 {}월 {}일".format(year, month, day)
# print(date1)

# a = 10
# a_format = "{}".format(a)
# print(a_format)
# a_format = "{0:11d}".format(a)
# print(a_format)
# a_format = "{:011,d}".format(a)
# print(a_format)


# b = 25.2345678
# b_format = "{}".format(b)
# print(b_format)
# b_format = "{:.2f}".format(b)
# print(b_format)

# print("{:.2f}".format(b))


# list타입 format함수 사용
stus = ['홍길동',100,90,80]
print("이름 : {}, 국어 : {}, 영어 : {}, 수학 : {}".format(\
    stus[0],stus[1],stus[2],stus[3]))

print("이름 : {}, 국어 : {}, 영어 : {}, 수학 : {}".format(\
    *stus)) #전개연산자 (*)


bank = [1,'홍길동',100000]
# 1번 홍길동 100,000원 - format 함수사용

print("{}번 {} {:,d}원".format(*bank))
print("{}번 {} {:,}원".format(*bank))


name = "유관순"
rank = 3
result = 98.23456

## 이름 : 유관순, 단계 : 3, 성공률 : 98.23%
print("이름 : {}, 단계 : {}, 성공률 : {:,.2f}%".format(name, rank, result))

## f 함수
print(f"이름 : {name}, 단계 : {rank}, 성공률 : {result:,.2f}%")











print("-"*30)