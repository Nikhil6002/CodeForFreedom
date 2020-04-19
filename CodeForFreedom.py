n = int(input())
lst1 = []
for i in range(n):
    ele = int(input())
    lst1.append(ele)

lst2 =[]
for i in range(n):
    val = str(input())
    lst2.append(val)

lst3 = lst2

zipped_list = zip(lst1,lst2)
sorted_pairs = sorted(zipped_list)
tuples = zip(*sorted_pairs)
lst1, lst2 = [ list(tuple) for tuple in  tuples]

for i in range (len(lst2)):
    if(lst2[i] == lst3[i]):
        continue
    elif (len(lst2[i]) == i+1):
        lst2[i] = lst2[i].upper()
    else :
        lst2[i] = lst2[i].lower()

print(lst2)