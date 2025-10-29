
# None : 거짓을 나타내는 자료형 / 반환값이 없는

print("-"*50)


### 5~21까지 출력

# for i in range(5,22):
#     print(i,end=" ")
# print()

# ### 1~10까지 출력

# for i in range(1,11):
#     print(i,end=" ")
# print()

# ### 0~9까지 홀수 출력,

# for i in range(10):
#     if i%2 == 0:
#         continue
#     print(i,end=' ')
# print()


### 구구단

# for i in range(2,10):
#     if i%2 == 0: continue
    
#     print(f"[ {i} 단 ]")
#     for y in range(1,10):
#         print("{} * {} = {}".format(i,y,i*y), end="\t")
#     print()
# print()


# for 변수 in 범위 (range, list, 문자열, 딕셔너리, 튜플)

# names = ['홍길동','김철수','이영희']

# for name in names:
#     print(name)
    
# for key, name in enumerate(names):
#     print(f"{key+1}.{name}")

# for name in range(len(names)):
#     print(f"{name+1}.{names[name]}")


# n_list = [
#     [1,'홍길동'],
#     [2,'김철수'],
#     [3,'이영희']
# ]

# for ns in n_list:
#     for n in ns:
#         print(n,end="\t")
#     print()


a_list = []

# for문을 사용해서 0이 10개 들어가는 리스트를 만드시오

# append 함수
# for i in range(10):
#     a_list.append("0")
    
# print(a_list)

# 리스트 타입 변환
a_list = list("0"*10)
# a_list = list(range(10))
print(a_list)

# 리스트 내포
a_list = ['0' for _ in range(10) ]
print(a_list)










### if문 간략화
# a = [1,2,3,4]
# result = [num * 3 for num in a if num%2 == 0]
# print(result)



### 2개 이상의 리스트를 순회
# names = ['홍길동','김철수','이영희']
# korean = [85,25,67]
# english = [90,25,56]

# for name, kor, eng in zip(names, korean, english):
#     print(f"{name}: 국어 {kor}점, 영어 {eng}점")


### 함수
# def aa(a, b): # a,b 매개변수 parameter
#     return a+b

# print (aa(1,2)) # 1,2 인수 arguments

### 가변 매개변수, 키워드 매개변수

# def mix_func(name, *args, **kwargs):
#     print(f"이름 : {name}")
#     print(f"추가 인수들 : {args}")
#     print(f"키워드 인수들 : {kwargs}")


# print(mix_func('홍길동',1,2,3,age=25, city='서울'))




print("-"*50)