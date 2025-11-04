
# 클래스 - 변수 접근제한 설정 가능

class Car:
    # color = "" # 전역변수
    # speed = 0
    
    # 생성자 : 객체 선언시 값을 바로 할당 할 수 있도록 함
    def __init__(self, color, speed): # 지역변수
        self.color = color
        self.speed = speed
        self.tire = 4
    
    
    # 클래스내 함수 첫번째 매개변수는 self
    def upSpeed(self,num):  # self = global
        # 클래스내 변수를 선택
        self.speed += num
        
    def downSpeed(self,num):
        self.speed -= num
        

# 객체선언 : 참조변수 = 클래스명

# c1 = Car() # 객체선언

# print(c1.speed)  # 참조변수(c1).변수명,  참조변수명(c1).함수명

# c1.upSpeed(10) # 클래스 내 함수 호출 - 참조변수.함수명()
# print(c1.speed)


# ### 속도 50으로 증가, 속도 30 감소, 속도 100

# c1.upSpeed(50)
# print("speed : ", c1.speed)
# c1.downSpeed(30)
# print("speed : ", c1.speed)
# c1.upSpeed(100)
# print("speed : ", c1.speed)
# c1.color = "파랑"
# print("color : ", c1.color)
    
# 2. 생성자를 통해 값지정    

c2 = Car('파랑',100) #생성자의 매개변수와 갯수 동일
print(c2.color)
print(c2.speed)
c2.upSpeed(200)
print(c2.speed)
c2.door = 5 # 클래스에 변수가 없으면 자동으로 추가된다
print(c2.door)
print(c2.tire)

