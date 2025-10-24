

# print("%d" % (100,220)) # error

# print("%d %d" % 100) # error

# print("%d %d" % (100,200)) # ok

# print("%20s" % "testtest")

str1 = "이름"
str2 = "국어"

name = input("이름 입력 : ")
kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))

total = kor+eng+math
avg = total / 3

print("-"*50)
print("%s\t%s\t%s\t%s\t%s\t%s" % ("이름", "국어", "영어", "수학", "합계", "평균")) # \n 줄바꿈 \t 탭키적용
print("-"*50)
print("%s\t%3d\t%3d\t%3d\t%3d\t%.2f" % (name, kor, eng, math, total, avg))
print("-"*50)