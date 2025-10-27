
print("-"*30)


# year = input("년도를 입력 :")
# month = input("월을 입력 :")
# day = input("일을 입력 :")

# print("%s년 %s월 %s일" % (year, month, day))


# a = 758.1234578
# print("%.2f" % a)

# b = 25.05
# print("%010.1f" % b)


# c = 150.15
# # print("%d  %.2f  %s" % (int(c), float(c), str(c)))
# print("%d  %.2f  %s" % (c,c,c))

# d = "*"
# print("%s" % d*20)


# num1 = int(input("숫자를 입력"))
# num2 = int(input("숫자를 입력"))

# print("%d + %d = %d" % (num1, num2, num1+num2))
# print("%d - %d = %d" % (num1, num2, num1-num2))
# print("%d * %d = %d" % (num1, num2, num1*num2))
# print("%d / %d = %d" % (num1, num2, num1/num2))
# print("%d // %d = %d" % (num1, num2, num1//num2))
# print("%d %% %d = %d" % (num1, num2, num1%num2))


# kor = int(input("국어점수를 입력"))
# eng = int(input("영어점수를 입력"))
# math = int(input("수학점수를 입력"))

# total = kor + eng + math
# avg = (kor + eng + math)/3

# print("\n"+" "*10+"[학생 성적 프로그램]")
# print("-"*50)
# print("국어\t영어\t수학\t합계\t평균")
# print("-"*50)
# # print("%d\t%d\t%d\t%d\t%.2f" % (kor, eng, math, total, avg))
# print("{0:d}\t{1:d}\t{2:d}\t{3:d}\t{4:.2f}".format(kor, eng, math, total, avg))




# fruit_code = {"사과":101, "배":102, "딸기":103}
# fruit_code2 = {"오렌지":105}

# fruit_code.update(fruit_code2)
# fruit_code.clear()

# print("%s" % type(fruit_code))


# print(fruit_code.keys())
# fruit_list = list(fruit_code.keys())
# print(fruit_list[2])

# fruit_items = list(fruit_code.items())

# print(fruit_items[0][0])

# a = [1,2,3,4,5]
# s = [i**2 for i in a if i > 3]
# print(s, 'aa', "bb", sep = "/")

a = 0.123456789012345679

# print("{0:.2f}\t{0:5f}".format(a))

# n = input("name : ")
# print("당신의 이름은 {} 입니다".format(n))


import datetime

now = datetime.datetime.now()

# jumin = "070101-1111111"

# if int(jumin[7]) < 3:
#     jumin2 = "19"+jumin[0:2]
#     jumin2 = 1900+int(jumin[0:2])
# else:
#     jumin2 = "20"+jumin[0:2]
#     jumin2 = 2000+int(jumin[0:2])
    
# age = now.year - int(jumin2)

# print(age)


# "071001-1111111"

jumin = input("주민번호를 입력 : ")

if jumin[7] == "1" or jumin[7] == "3":
    print("남자")
else:
    print("여자")


if int(jumin[2:4]) == now.month:
    print("%s 월 이벤트 대상자" % jumin[2:4])
else:
    print("%s 월 이벤트 대상자 아님" % jumin[2:4])


str1 = "안녕하세요"

if "하" in str1:
    print("글자 존재")
else
    print("글자 없음")

print("-"*30)