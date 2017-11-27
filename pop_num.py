# pop_num.py
import random
t_list = tuple(range(1,46))
l_list = []
for i in t_list:
    l_list.append(i)

print l_list

count = 0
fnum = []
while count < 7:
    fnum.append(l_list.pop(random.randint(0,len(l_list)-1)))
    count += 1
    print fnum

print sorted(fnum)
