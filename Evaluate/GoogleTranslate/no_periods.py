# args: [filename]

import sys

f = open(sys.argv[1],'r')
n = open('Updated'+sys.argv[1],'w')

lines = f.readlines()
f.close()

for line in lines:
	if line.strip()[len(line.strip())-1] == '.':
		to_write = line.strip()[:len(line.strip())-1]
	else:
		to_write = line.strip()
	n.write(to_write+'\n')
	print(to_write)
n.close()
