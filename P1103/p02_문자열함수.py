
# ### 문자열 
# # a = "안녕하세요"

# # print(a[2:4])        # 슬라이싱
# # print("안녕"*3)       # 반복
# # print("안녕"+"hello") # 연결연산자

# a = "abc"
# print(a.upper()) # 대문자로 변경

# a = "ABC"
# print(a.lower()) # 소문자로 변경

# # swapcase() # 대문자를 소문자, 소문자를 대문자로 변경
# # title() - 첫글자를 대문자로

# ### 문자열 찾기
# a = "11223333345"
# print(a.count("1"))  # 해당되는 문자 갯수

# b = "프로그램 중 파이썬 사용자가 제일 많습니다.(파이썬 프로그램)"
# print(b.find("파이썬"))  # 왼쪽부터 해당위치 검색, 없을때 -1출력
# print(b.rfind("파이선"))  # 오른쪽부터 해당위치 검색, 없을때 -1출력
# print(b.count("파이썬"))
# print(b.index("파이썬")) # 위치 검색, 없을때 오류 출력(error)

# print(b.startswith("로")) # 해당문자로 시작되는지 확인, true
# print(b.endswith("프")) # 해당문자로 끝나는지 확인, true


# ### 공백제거
# # strip() - 좌우 공백제거, 문자사이 공백은 제거되지 않음
# # a = input("아름을 입력 : ").strip()
# # rstrip() - 오른쪽 공백제거
# # lstrip() - 왼쪽 공백제거

# print(b.replace(' ','')) # 문자열 변경,  replace(변경하려는 문자, 변경 후 문자)

# ### 문자열 분리 - 타입은 리스트로 분리
# # split() 
# a = "1,홍길동,100,100,100,300"
# a_list = a.split(",")
# print(a_list)

# titles = ['번호','이름','국어','영어','수학','합계','평균']
# print(*titles,sep="\t") # sep 사이 간격출력(키워드 매개변수)

# a_list = a.split(",")

# # print(sep:변수사이사이 모두 적용, end:마지막에 적용(키워드 매개변수))
# print(*a_list, sep="\t", end="**")
# print()

# # join() - 문자열 결합
# ss = "%"
# print(ss.join("파이썬"))

# # map() : 리스트를 입력받아 처리하는 함수

# # a = ["100","90","80"]
# # b = []
# # for i in a:
# #     b.append(int(i))
    
# # print(a)
# # print(b)

# #  ==> 간략화
# a = ["100","90","80"]
# b = list(map(int,a)) #map타입객체로 저장    map(function함수부분, 리스트데이터)

# print(a)
# print(b)


# map(function함수부분, 리스트데이터)
# def multi(x):
#     return x*2

# a = [1,2,3]

# b = list(map(multi,a))
# print(b)

# isdigit() : 숫자인지 확인
# isalpha() : 문자(영문자, 한글)인지 확인
# isalnum() : 문자, 숫자인지 확인 (특수문자 포함시 False)
# islower() : 소문자 확인
# isupper() : 대문자 확인

a = "~ 11abc"
print(a.isalnum())


