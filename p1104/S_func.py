
class Student:
    
    def __init__(self, stuno,name,kor,eng,math):
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
    
    def sum(self):
        return self.kor+self.eng+self.math
    
    def avg(self):
        return self.total/3
    

# 학생성적들을 저장하는 공간
class Stuscore:
    
    stu_list = []
    titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
        
    def add(self,s):
        self.stu_list.append(
            {'stuno':s.stuno,'name':s.name,'kor':s.kor,'eng':s.eng,'math':s.math,'total':s.total,'avg':s.avg,'rank':s.rank}
        )   
        
    def print(self):
        
        print()
        print(" "*20,"[ 학생성적리스트 ]")
        print("-"*65)
        #print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        print(*self.titles,sep="\t")
        print("-"*65)
        
        for stus in self.stu_list:
            print(f"{stus['stuno']}\t{stus['name']}\t{stus['kor']}\t{stus['eng']}\t{stus['math']}\t{stus['total']}\t{stus['avg']:.2f}\t{stus['rank']}")
            
        print()           
        
