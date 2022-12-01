wd = input().upper()
wd_set = list(set(wd))
li = []
for i in wd_set:
    li.append(wd.count(i))
if li.count(max(li)) > 1:
    print('?')
else:
    print(wd_set[li.index(max(li))])