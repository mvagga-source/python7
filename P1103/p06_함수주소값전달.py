
def val(a,b):
    a = 100
    b = 50

a = 1
b = 2
print(a,b)

val(a,b)
print(a,b)


# 복합변수 (함수 외부에서도 값이 변경됨)   
def val(a):
    a[0] = 100
    
a = [1,2]
val(a) # 주소값이 전달됨(얕은복사)

val(a[0],a[1]) # 값이 전달됨


b = a # 얕은복사 주소로 공유됨
b = [*a] # 깊은복사 데이터값 복사