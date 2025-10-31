
# stu_list = [name:"홍길동",kor:100,eng:100,math:100]
# stu_list = {키:값,키:값,키:값...} # 쌍 2개가 하나로 묶인 자료구조

# 딕셔너리 생성
list1 = [1,2,3]
dic1 = {1:'a',2:'b',3:'c'}
dic2 = {"no":1,"name":"홍길동","class":3}

print(dic1)

# 딕셔너리 추가
stu = {"학번":1,"이름":"홍길동","학과":"컴퓨터공학"}
print(stu)
stu['연락처'] = "010-1111-1111"
print(stu)

# 딕셔너리 수정
stu['이름'] = "고길동"
print(stu)

# 딕셔너리 삭제
del(stu["이름"])
print(stu)