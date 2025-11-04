

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
    
    # def add_f(self, s):
    #     self.stu_list.append(
    #         {'stuno':s.stuno,'name':s.name,'kor':s.kor,'eng':s.eng,'math':s.math,'total':s.total,'avg':s.avg,"rank":s.rank}
    #     )


class Stuadd:
    
    stu_list = []
    titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
        
    def add_f(self,s):
        self.stu_list.append(
            {'stuno':s.stuno,'name':s.name,'kor':s.kor,'eng':s.eng,'math':s.math,'total':s.total,'avg':s.avg,'rank':s.rank}
        )   
        
        
    def rank_f(self):

        for i in self.stu_list:
            c = 1
            for j in self.stu_list:
                
                if i['total'] < j['total']:
                    c += 1
            i['rank'] = c        
            
    def print_f(self):
        
        for i in self.stu_list:
            print(f"{i['stuno']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']:.2f}\t{i['rank']}")


    
s1 = Stu(10101,"홍길동",100,100,100)
s2 = Stuadd()
s2.add_f(Stu(10101,"홍길동",100,100,100))
s2.add_f(Stu(10101,"고길동",80,70,10))
s2.add_f(Stu(10101,"이길동",100,90,20))
print(s2.stu_list)
s2.rank_f()
print(s2.stu_list)
s2.print_f()



        
    

        

