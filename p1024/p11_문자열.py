

#문자열 선택

name = "안녕하세요"

print("-"*30)

# print(name[0])
# print(name[-5])

# 문자슬라이싱

print(name[0:2]) # 0부터 2앞까지 출력 (0-1)
print(name[:2])  # 상동

# 문자길이
print(len(name))

# 슬라이싱 - 스탭
print(name[::2]) # 모든 문자열 2칸씩 띄워 출력
print(name[::-1]) # 반대로 출력


# 880101-2111111
jumin = "880101-1111111"

print(jumin[-7])

if (int(jumin[-7])%2 == 0):
    print("여자")
else:
    print("남자")




print("-"*30)