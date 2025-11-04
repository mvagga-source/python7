
# 예외처리 - 오류가 발생해도 계속실행

# 구문오류 : 작업자 오타, 실행하기전 오류
# 런타임 오류 : 프로그램 실행중 오류

# a_list = [1,2,3]
# try:
#     print(a_list[100])
# except Exception as e: # as 별칭으로 오류 확인 가능
#     print(e)

# print("프로그램종료")
    
# 외부연결 : 파일출력, 읽기,쓰기,프린터기 연결, db연결

print(1)
print(2)
try:
    print(3)
    # 에러
    # raise SyntaxError # raise : 강제로 에러발생하는 명령어
    raise KeyError
    print(4)
    print(5)
except: # 에러발생시 실행
    print(6)
finally: # 에러여부와 상관없이 실행
    print(7)
print(8)

# ValueError : 값 오류
# indexError : 인덱스 오류
# Exception : 모든 예외를 처리 (맨밑에 위치함)