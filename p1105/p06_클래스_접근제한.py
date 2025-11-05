
class cal:
    __hour = 12 # "__" 접근제한
    minute = 30
    second = 20
    
    def setHour(self, hour):
        if hour>23:
            print("23보다 큰수는 입력을 할 수 없습니다.")
            return 
        self.__hour = hour
    def getHour(self):
        return self.__hour
    
time = cal()

print(time.getHour())
print(time.setHour(15))
print(time.getHour())

print(time.__hour)


