
a_list = [1,2,3]

# list 추가 - append(맨뒤 추가), insert(위치,값), extend(리스트 병합)

# print(a_list)
# a_list.append(10) # 파괴적, 비파괴적(a+100)
# print(a_list)
# a_list.insert(0,200)
# print(a_list)
# a2_list = [5,6,7]
# a_list.extend(a2_list)
# print(a_list)

# a_list = a_list + [10,20]
# print(a_list)

# list 삭제 - pop(맨뒤 삭제), del(해당위치 삭제), remove(해당값 삭제), clear(모두삭제)

aa_list = [1,2,3,4,5,6,7]
print(aa_list)
aa_list.pop()
print(aa_list)
del aa_list[0]
print(aa_list)
aa_list.remove(5)
print(aa_list)
aa_list.clear()
print(aa_list)


# []   리스트 1개 : 1차원 리스트
# [[]] 리스트 2개 : 2차원 리스트

b_list = [
    ["홍길동", 100, [1,2,3]], ["이순신",200]
]