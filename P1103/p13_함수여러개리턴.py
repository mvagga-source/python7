
### 
# 파이썬은 여러개 리턴이 가능
# 리턴형태 : 튜플타입
# 리스트 형태로 값을 리턴하면 여러개의 값을 리턴할수 있름


# 튜플 타입으로 여러개 리턴
def cal():
    return 10, 20, 30  # 파이썬만 여러개 리턴 가능

a, b, c = cal() # 튜플 형태로 넘어옴
print(a,b,c)

# 리스트로 리턴
def func():
    a_list = [10,20,30]
    return a_list

a_list = func()
print(a_list)

