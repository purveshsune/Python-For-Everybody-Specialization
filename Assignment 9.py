fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
c= dict()
for line in fh:
    if line.startswith("From"):
        words=line.split()
        if len(words) > 2 and words[0] == 'From':
            email = words[1]
            c[email] = c.get(email,0) + 1
bigc = None
bige = None
for words in c:
  value = c[words]
  if bigc == None or value > bigc:
    bigw = words
    bigc = value

print (bigw, bigc)
