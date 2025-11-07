
class StusClass():
    
    stu_titles = ['학번','이름','국어','영어','합계','평균','성적']        

    def print_f(self, s):
        
        print("-"*60)
        print("~~ 학생성적 출력 ~~")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*self.stu_titles))
        print("-"*60)
        
        for i in range(len(s.stu_list)):
            print(f"{s.stu_list[i][0]}\t{s.stu_list[i][1]}\t{s.stu_list[i][2]}\t{s.stu_list[i][3]}\t{s.stu_list[i][4]}\t{s.stu_list[i][5]}\t{s.stu_list[i][6]}")    
        print("-"*60)
        print()    
        
    def modify_f(self, s):
        print("-"*60)
        print("~~ 학생성적 수정 ~~")
        print("-"*60)
        
        
    
    def delete_f(self, s):
        pass
    
    def rank_f(self,s):
        pass
    
    