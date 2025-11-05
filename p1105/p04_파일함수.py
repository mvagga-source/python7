
import os

# # 현재 위치에 존재하는 모든 파일 출력
# print(os.listdir("c:\\down\\"))

# #
# fname = input("검색 파일이름 >> ")

# # 파일 존재 여부 확인
# if os.path.exists("c:\\down\\"+fname):
#     print("존재")
# else:
#     print("없음")
    
### 파일복사    
# 파일읽기 rb, 파일쓰기 wb
f = open("c:\\down\\nct1.jpg","rb")
f2 = open("c:\\aaa\\nct1.jpg","wb")
    
# read() : 파일읽기   readline(), readlines() : 문자일기
while True:
    nctfile = f.read(1) # 1byte
    if not nctfile: break
    f2.write(nctfile)
    
f.close()
f2.close()
print("복사완료!!")