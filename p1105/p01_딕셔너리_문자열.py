
import os

# stu_list = [
#     [10101,'홍길동',80,80,80,240,80.00,0],
#     [10102,'유관순',90,90,90,280,90.00,0],
#     [10103,'이순신',100,100,100,300,100.00,0]
# ]

stu_list = [
    {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0},
    {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
        'total':270,'avg':90.00,'rank':0},
    {'stuno':10102,'name':'이순신','kor':100,'eng':100,'math':100,\
        'total':300,'avg':100.00,'rank':0}
]

# 출력
# for stu in stu_list:
#     print(f"{stu['stuno']}\t{stu['name']}\t{stu['kor']}\t{stu['eng']}\t{stu['math']}\t{stu['total']}\t{stu['avg']}\t{stu['rank']}")

##### 딕셔너리 -> 문자열 형식으로 전환
with open("c:\\down\\aaa.txt","w",encoding="utf8") as f:

    stu_str = ""
    for idx in range(len(stu_list)):
        stu_str += f"\
{stu_list[idx]['stuno']},\
{stu_list[idx]['name']},\
{stu_list[idx]['kor']},\
{stu_list[idx]['eng']},\
{stu_list[idx]['math']},\
{stu_list[idx]['total']},\
{stu_list[idx]['avg']},\
{stu_list[idx]['rank']\
}\n"

    # 파일로 저장
    f.write(stu_str)

##### 문자열 -> 딕셔너리
with open("c:\\down\\aaa.txt","r",encoding="utf8") as f:
    
    while True:
        txt = f.readline()
        if txt == "": break
       
        t_list = txt.strip().split(",")
        t_dic = {\
            'stuno':int(t_list[0]),\
            'name':t_list[1],\
            'kor':int(t_list[2]),\
            'eng':int(t_list[3]),\
            'math':int(t_list[4]),\
            'total':int(t_list[5]),\
            'avg':float(t_list[6]),\
            'rank':int(t_list[7])\
        }
        
        print(t_dic)
            


# f.close()
    
