# グループに振り分ける方法②の改良【任意の人数】または【任意の人数とグループ数】
import random

member_num = random.randint(1, 40) # 範囲が知りたい
group_num = random.randint(1, 10)  # 範囲が知りたい

group1_size = member_num // group_num
group2_size = group1_size + 1

group2_num = member_num % group_num
group1_num = group_num - group2_num

set_num = []
for i in range(group_num):
  if i < group1_num:
    set_num.append(group1_size)
  else:
    set_num.append(group2_size)

print('グループ人数が' + str(member_num) + 'でグループの数が' + str(group_num) + 'の場合')
print('グループ : ', set_num)
