import sys

f = open(sys.argv[1],'r')
n = open('Updated'+sys.argv[1],'w')

lines = f.readlines()
f.close()
bad = [76,116,118,124,125,130,135,136,138,139,148,149,153]
num = 1
count = 0
for line in lines:
    if num not in bad:
        n.write(line)
        count += 1
    num += 1

n.close()
print(count)
