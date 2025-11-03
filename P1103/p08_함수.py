
### 가변 매개변수
# def add(a,b,*c): #변수 앞에 *를 붙이면 가변매개변수가 됨
    
#     print(c) # c : 리스트 형식
    
#     sum = a+b
#     for i in c: # c:여러개 가능
#         sum += i
        
#     return sum

# print(add(1,2,3,4,5,6,7))


# def print_str(a,b,*c):
#     print(a)
#     print(b)
    
#     for i in c:
#         print(i)
        
# print_str("안녕",'홍길동',1,2,3)


### 5번 입력받아 함수를 사용해서 출력
# def print_str(*c):
#     for i in c:
#         print(i)
        
# str_list = [0,0,0,0,0]
        
# for i in range(5):
#     str_list[i] = input("입력하세요 : ")
#     # str_list.append(str)
    
# print_str(*str_list)


stus = [1,'홍길동',100,90,80]

def sum(kor,eng,math):
    return kor+eng+math

def avg(kor,eng,math):
    return (kor+eng+math)/3

# stus = [1,'홍길동',100,90,80,270,90.00]

stus.append((sum(stus[2],stus[3],stus[4])))
print(stus)
stus.append((avg(stus[2],stus[3],stus[4])))
print(stus)
