fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
c ={}
for line in fh:
    if not line.startswith("From"):continue
    xyz = line.split()
    time = xyz[5]
    abc = time.split(':')
    hour = abc[0]
    c[hour] = c.get(hour,0) + 1
for k, v in sorted(c.items()):
    print (k,v)
