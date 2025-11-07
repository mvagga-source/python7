
class StuClass():

    stu_list = []  
      
    def __init__(self):
        
        self.stuno = 10101
        self.name = ""
        self.kor = 0
        self.eng = 0
        self.total = 0
        self.avg = 0
        self.rank = 0
    
    def menu_f(self):
        
        print("-"*50)
        print("[학생성적관리 프로그램]")
        print("1. 학생성적입력")
        print("2. 학생성적출력")
        print("3. 학생성적수정")
        print("4. 학생성적삭제")
        print("5. 등수관리")
        print("0. 프로그램종료")
        print("-"*50)
        print()
    
    def input_f(self):
        
        self.name = input("이름 입력 : ")
        self.kor = int(input("국어점수 입력 : "))
        self.eng = int(input("국어점수 입력 : "))
        
        self.total_f()
        self.avg_f()
        
        self.stu_list.append([self.stuno, self.name, self.kor, self.eng, self.total, self.avg, self.rank])
        print(self.stu_list)
        
    def total_f(self):
        self.total = self.kor+self.eng
    
    def avg_f(self):
        self.avg = self.total/2
        