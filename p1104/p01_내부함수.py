
### 내부함수 : 함수내의 함수정의가 가능
# def outFunc(a,b):
#     def inFunc(n1,n2):
#         return n1+n2
#     return inFunc(a,b)

# print(outFunc(1,2))


#lambda() 함수 - 함수를 한줄로 간략화

def add(a,b):
    return a+b

print(add(10,20))

# ==> 축약

## lambda 선언 / 한줄 이상의 문장 작성은 불가함
# result : 함수명(값,값)
result = lambda a,b : a+b # 매개변수 선언 : 함수 수식
print(result(10,20))

result = lambda a:a**2
print(result(10))

result = lambda a:a%2
print(result(3))


## map함수 : 여러개를 함수 적용시킬때 사용
# 결과값(리스트) = map(함수,리스트) 객체 : 리스트타입으로 변경


def cal(a):
    return a*10

my_list = [1,2,3,4,5]

# m_list = list(map(cal,my_list))
m_list = list(map(lambda a:a*10,my_list))
print(m_list)

m_list = list(map(lambda a:a+100,my_list))
print(m_list)

m_list = list(map(lambda a:"{}원".format(a*1425),my_list))
print(m_list)

my_list = ['0']*10
m_list = list(map(lambda a:int(a),my_list))  # 문자형식을 숫자형식으로 일괄 변경
print(m_list)