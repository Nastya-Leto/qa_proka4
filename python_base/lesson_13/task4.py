
sp = [1,2,2,3,4,7,5,6,7,7]
number = 0
count_num=0

for c in sp:
    if sp.count(c)>count_num:
        count_num=sp.count(c)
        number=c
print(number)