
class Student:
    
    def __init__(self,stuno,name,kor,eng,math):
        # 클래스 전역변수 = 함수내에 사용하는 지역변수
        # self 사용시 전역변수로 자동 생성 및 값 지정됨
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
        
    # 합계
    def total_f(self):
        self.total = self.kor+self.eng+self.math
        
    def avg_f(self):
        self.avg = self.total/3
        



#매개변수 __init__ 함수 매개변수 개수와 맞아야 함

s = Student(10101,"홍길동",70,80,90)

print("국어 : ",s.kor)
print("합계 : ",s.total)
print("평균 : ",s.avg)
s.kor = 100
s.total_f()
s.avg_f()
print("국어 : ",s.kor)
print("합계 : ",s.total)
print("평균 : ",s.avg)

