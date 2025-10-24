
print("-"*30)

# // : 몫, % : 나머지, ** : 제곱

# print(10/3)
# print(10//3)
# print(10%3)
# print(10**3)

# 두수를 입력받아 위의 연산을 출력 하시오

# for a in range(1,3):

#     num1 = int(input("숫자를 입력 : "))
#     num2 = int(input("숫자를 입력 : "))

#     print(num1+num2)
#     print(num1-num2)
#     print(num1*num2)
#     print(num1/num2)
#     print(num1//num2)
#     print(num1%num2)
#     print(num1**num2)

# 780원 동전으로 교환
# 500, 100, 50, 10 동전 몇개로 교환해야

# money = 1234567800

# money1 = money // 500
# print("500원 동전 : %d 개" % money1)

# money2 = money % 500
# # print("500원 나머지 : %d" % money2)

# money3 = money2 // 100
# print("100원 동전 : %d 개" % money3)

# money4 = money2 % 100
# # print("100원 나머지 : %d" % money4)

# money5 = money4 // 50
# print("50원 동전 : %d 개" % money5)

# money6 = money4 % 50
# # print("50원 나머지 : %d" % money6)

# money7 = money6 // 10
# print("10원 동전 : %d 개" % money7)


coin = 1597000

# 50000, 10000, 5000, 1000

# m1 = coin // 50000
# m2 = coin % 50000
# print("50,000원 : %d 개" % m1)

# m3 = m2 // 10000
# m4 = m2 % 10000
# print("10,000원 : %d 개" % m3)

# m5 = m4 // 5000
# m6 = m4 % 5000
# print("5,000원 : %d 개" % m5)

# m7 = m6 // 1000
# print("1,000원 : %d 개" % m7)


for a in [50000, 10000, 5000, 1000]:
    m1 = coin // a
    m2 = coin % a
    
    coin = m2
    
    print("%d원 : %d 개" % (a, m1))





print("-"*30)