

### list 자동생성 방법

# a_list = [1,2,3,4,5,6,7,8,9]
# print(a_list)

# b_list = list(range(1,10))
# print(b_list)

# c_list = [i for i in range(1,10)]
# print(c_list)

# d_list = ['0','0','0','0','0','0','0','0','0']
# print(d_list)

# e_list = list('0'*9)
# print(e_list)

# f_list = ['0' for _ in range(9)]
# print(f_list)

# --------------------------------------------------

## 3*3 리스트 형태
# a_list = list(range(1,10))
# b_list = []
# # print(a_list)
# i_list = []

# for i in a_list:
#     print(i, end=" ")
    
#     i_list.append(i)
    
#     if i%3 == 0:
#         b_list.append(i_list)
#         i_list = []
#         print()
    
# print(b_list)


# # ## 4*4 리스트 형태
# for i in range(1,17):
#     print(i, end=" ")
#     if i%4 == 0:
#         print()        
        
# # ## 5*5 리스트 형태
# for i in range(1,26):
#     print(i, end=" ")
#     if i%5 == 0:
#         print()           



# a_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for aa in a_list:
#     for a in aa:
#         print(a,end=" ")
#     print()



# a_list = [9,1,2,5,6,8,3,4,7]

# for i in range(0,len(a_list)):
#     print(a_list[i],end="\t")
#     if (i+1)%3 == 0:
#         print()
        
# for key, val in enumerate(a_list):
#     print(val,end="\t")
#     if (key+1)%3 == 0:
#         print()
        
import random

a_list = list(range(1,17))
random.shuffle(a_list)
print(a_list)

for key, val in enumerate(a_list):
    print(val,end="\t")
    if (key+1)%4 == 0:
        print()

