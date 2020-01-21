fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    a=line.split()
    i=0
    for z in a:
        if z not in lst:
            lst.append(z)
    else:
        continue
lst.sort()
print (lst)
