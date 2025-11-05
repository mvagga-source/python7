
import os

# 스트림(연결통로) : 파일열기 / 모드 r(읽기) w(쓰기) a(추가)
# f = open("C:\\workspace\\python7\\p1105","r",encoding="utf8") - "\" 단독 사용시 줄바꿈으로 인식함
# f = open("C:/down/aaa.txt","r",encoding="utf8")  # euc-kr : 국내표준, utf-8, utf8 : 국제표준


##### 읽기 모드

# f = open("C:\\down\\aaa.txt","r",encoding="utf8")

### readline()
# while True:
#     txt = f.readline() # read() - 속도느림, readline() - 1줄, readlines() - 전체
#     if txt == "": break
#     print(txt, end="") # readline()의 경우 enter값 삭제필요

### readlines : 전체 가져오기(리스트 형식)
# txt_list = f.readlines() 
# for txt in txt_list:
#     print(txt,end="")

### read : 1byte싹
# while True:
#     txt = f.read() 
#     if txt == "": break
#     # print(txt,end="")
#     print(txt)

##### 쓰기 모드
# f = open("C:\\down\\ccc.txt","w",encoding="utf8")
##### 추가 모드
# f = open("C:\\down\\ccc.txt","a",encoding="utf8")

# stu_data = ""
# for _ in range(3):
#     txt = input("입력 >> \n")
#     stu_data += txt+"\n"
# f.write(stu_data)

# f = open("C:\\down\\ccc.txt","a",encoding="utf8")
# for i in range(5):
#     f.write(f"안녕하세요. {i}\n")

# f = open("C:\\down\\aaa.txt","r",encoding="utf8")

# while True:
#     txt = f.readline()
#     if txt == "":break
#     print(txt.strip())

# f.close()

# close() 자동포함
with open("C:\\down\\aaa.txt","r",encoding="utf8") as f:
    
    while True:
        txt = f.readline()
        if txt == "":break
        print(txt.strip())
    

