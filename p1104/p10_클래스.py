

class Stu:
    
    stu_list = []    
    
    def __init__(self,stuno,name,kor,eng,math):
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
    
        
    def total_f(self):
        self.total = self.kor+self.eng+self.math
        
    def avg_f(self):
        self.avg = self.total/3
        
    def rank_f(self):
        pass
    
    def add_f(self, s):
        self.stu_list.append(
            {'stuno':s.stuno,'name':s.name,'kor':s.kor,'eng':s.eng,'math':s.math,'total':s.total,'avg':s.avg,"rank":s.rank}
        )
    
s1 = Stu(10101,"홍길동",100,100,100)
s1.add_f(s1)
print(s1.stu_list)
        
    

        

