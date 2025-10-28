print("-"*30)


# for i in range(10):
#     print(i, end = "\t")
# print()


# sum = 0
# for i in range(1,101):
#     sum = sum + i
#     if sum > 100:
#         break
# # print(i, sum)
# print(f"{i}번째 : {sum}")


result = 1
for i in range(1,11):
    result = result * i
    if result > 100:
        break
print("{} 번째 : {:,}".format(i, result))






print("-"*30)