# encoding: utf-8
# author = ‘LW’

users = []

users.append((1, 'Liu Wei', 29, '18500000001'))
users.append((2, 'Li Si', 28, '18600000002'))
users.append((3, 'Zhang S', 30, '18700000003'))


find_user = None
find_user_list = list((x for x in users if x[0]==1))

print(find_user_list)

if(len(find_user_list)>0):
    find_user =  find_user_list[0]


edit_info = 'lw,40,123'
print((find_user[0],)+tuple(edit_info.split(',')))
users[users.index(find_user)] = (find_user[0],)+tuple(edit_info.split(','))


print(users)