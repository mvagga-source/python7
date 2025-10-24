
#국어, 영어, 수학점수를 입력받아 합계와 평균을 출력하시오

kor = int(input("국어 점수 입력 "))
eng = int(input("영어 점수 입력 "))
mas = int(input("수학 점수 입력 "))

print("합계 :",kor+eng+mas)

print("평균 :",(kor+eng+mas)/3)
print("평균 : %.2f" % ((kor+eng+mas)/3))