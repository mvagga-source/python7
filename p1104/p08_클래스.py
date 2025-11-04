
### 기본구조
# class Student:
#     stuno = 0
#     name = ""
#     kor = 0
#     eng = 0
#     math = 0
#     total = 0
#     avg = 0
#     rank = 0
    
#     def sum(self):
#         return self.kor + self.eng + self.math
        
#     def avg(self):
#         return self.total/3
    
# s1 = Student()
# s1.stuno = 1
# s1.name = "홍길동"
# s1.kor = 100
# s1.eng = 90
# s1.math = 80
# s1.total = s1.sum()
# s1.avg = s1.avg()


# 학생 1명 저장하는 공간

# from S_func import *
    
# # s1 = Student(10101,"홍길동",80,100,70)
# # s1 = Student(10102,"고길동",100,100,100)
# # s1 = Student(10103,"이길동",80,100,70)

students = Stuscore()
students.add(Student(10101,"홍길동",80,100,70))
students.add(Student(10102,"고길동",100,100,100))
students.add(Student(10103,"이길동",80,100,70))

# students.print()