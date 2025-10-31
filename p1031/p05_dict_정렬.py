

### 딕셔너리 정렬

import operator

names = {"홍길동":100,"유관순":80,"이순신":90}

# reverse = True : 역순정렬, reverse = False : 순차정렬
# itemgetter(0) : 키, itemgetter(1) : 값
names2 = sorted(names.items(),key=operator.itemgetter(1), reverse=False)

print(names)
print(names2)


### 리스트 정렬

a_list = [1,5,9,4,3]

# sort() : 해당리스트 자체를 정렬, 원본변경
a_list.sort()
print("a_list : ",a_list)
a_list.reverse() # 순서가 변경
print("a_list : ",a_list)

# sorted() : 다른변수에 저장가능, 원본은 변경 안됨
# reverse=True : 역순정렬
b_list = sorted(a_list, reverse=True)
print("b_list : ",b_list)

### 리스트 최대값

print(max(a_list))
print(min(a_list))



