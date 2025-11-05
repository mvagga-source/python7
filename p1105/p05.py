

# 문자열 -> 딕셔너리 형식으로 전환

import ast

str = "{'stuno':10102,'name':'이순신','kor':100,'eng':100,'math':100,\
'total':300,'avg':100.00,'rank':0}"

str_dict = ast.literal_eval(str)

print(str_dict)

