
listjadou=[]

for i in range(20):
    if (i+1) % 2==1:
        if (i+1) not in [5,13]:
            listjadou.append(i+1)


print(listjadou) #résultat

del listjadou[len(listjadou)-1] #on supprime le dernier élément
print(listjadou)
del listjadou[len(listjadou)-5]
print(listjadou)


listjadou2=[0]
i=0
while i<=35:
    if i % 2==1:
        listjadou2.append(i)
    i=i+1
print(listjadou2)