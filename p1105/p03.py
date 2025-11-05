
import os

f = open("c:\\down\\bbb.txt",encoding="utf8") # 문자열 형식으로 저장됨 > 형변환이 필요함

# while True:
#     txt = f.readline()
#     if txt == "": break
#     # print(txt.strip()) 
#     print(txt, end="")
#     # print(txt)
    
# txt = f.readline()
# print(txt.strip())
# print(txt.split(","))
# print(txt.strip().split(","))
# print(txt.strip().split(",")[5])
# print(int(txt.strip().split(",")[5]))

b_list = []
while True:
    txt = f.readline()
    if txt == "": break
    # print(txt, end="")
    b_list.append(txt.strip().split(","))

print(b_list)

f.close()

# ////////////////////////////////////////////////////////////////////////////////////////////

f = open("c:\\down\\aaa.txt",encoding="utf8") # 문자열 형식으로 저장됨 > 형변환이 필요함

a_list = []
while True:
    txt = f.readline()
    if txt.strip() == "": break
    print(txt, end="")
    a_list.append(txt.strip().split(","))
    
print(a_list)

f.close()