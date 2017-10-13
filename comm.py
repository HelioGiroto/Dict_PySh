********************************************
** Equivalência do comando COMM em Python **
********************************************

a = [1, 2, 3, 7]
b = [2, 3, 8, 9]
c = [2, 3, 6, 11]
d = [1, 2, 3, 7]

comm = set(a) & set(b) & set(c) & set(d)

print("Em comum nas 4 listas:", comm)



# testar esse formato tb: c = list(set(a).intersection(set(b)))

# autor: Hélio Giroto
