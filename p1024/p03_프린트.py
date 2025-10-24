
# print() 다양한 출력

# print(100)
# print("합계")
# print("-"*30)

# print("100 + 100 =",200)

# # % print를 사용하면 소수점을 제어할 수 있음
# print("299/3 = ", (299/3))
# print("299/3 = %.3f" % (299/3))

kor = 100
eng = 100
math = 99

# %를 사용할때 정수 : d, 실수 : f
# 100 + 100 + 99 = 299
# print(kor,"+",eng,"+",math,"=",kor+eng+math)
# print("%d + %d + %d = %d" % (kor, eng, math,kor+eng+math))

print("%d" % (kor))
print("%5d" % (kor))
print("%05d" % (kor))
print("%010d" % (kor))

print("%20d" % (1000000))

print("%.2f" % (10.12345)) # .2f 소숫점 2자리까지 출력

print("합계 : %05d, 평균 : %.2f" % (299,99.6667))

