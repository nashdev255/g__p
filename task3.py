import random

member_num = random.randint(3, 42)
group_num  = 3
print('グループ人数が' + str(member_num) + 'グループの数が' + str(group_num))

group1_size = member_num // group_num
group2_size = group1_size + 1

group2_num = member_num % group_num
group1_num = group_num - group2_num

member_rand_list = []
for i in range(member_num):
  member_rand_list.append(i + 1)
random.shuffle(member_rand_list)

group_list = []
for i in range(group_num):
  group_list.append([])

t = 0
for i in range(group_num):
  if i < group1_num:
    for j in range(group1_size):
      group_list[i].append(member_rand_list[t])
      t += 1
  else:
    for j in range(group2_size):
      group_list[i].append(member_rand_list[t])
      t += 1

for i in range(group_num):
  print('グループ' + str(i + 1) + ' : ', group_list[i])
