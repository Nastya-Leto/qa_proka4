stroka = "this is great idea"
sp = stroka.split(' ')
print(sp)
dlina = 0

for slovo in sp:
    dlina += len(slovo)

srednee  = dlina/len(sp)
print(srednee)