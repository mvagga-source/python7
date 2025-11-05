
class Student:
       
    def __init__(self,stuno,name,kor,eng,math):
        
        # 객체변수 - 인스턴스
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0

    # 객체, 참조변수를 출력하면 함수실행이 됨
    def __str__(self):
        return f"{self.stuno}\t{self.name}"
        
    def s_total(self):
        self.total = self.kor+self.eng+self.math
        return self.total
        
    def s_avg(self):
        self.avg = self.total/3
        
class Students:
    
    stu_list = []
    
    def print_f(self):
        for stus in self.stu_list:
            # print(f"{stus['stuno']}\t{stus['name']}\t{stus['kor']}\t{stus['eng']}\t{stus['math']}\t{stus['total']}\t{stus['avg']:.2f}\t{stus['rank']}")
            print(stus.s_total())
    
    def add_f(self,student):
        self.stu_list.append(student)
        

# 학생성적 1명 입력
# stu_list = []
# stu_list.append(Student(10101,'홍길동',100,100,100))
# stu_list.append(Student(10101,'고길동',80,100,100))
# stu_list.append(Student(10101,'이길동',100,70,100))

# s1 = Student(10101,'이길동',100,70,100)
# print(s1)

# 클래스에서 리스트에 추가
s1 = Student(10101,'홍길동',100,100,100)
print(s1)


stus = Students()
stus.add_f(Student(10101,'홍길동',100,100,100)) # 객체전체가 리스트로 저장됨(주소값 형식)
stus.add_f(Student(10102,'고길동',80,100,100))
stus.add_f(Student(10103,'이길동',100,70,100))

print(stus.print_f())



