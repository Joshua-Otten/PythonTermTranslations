import sys

f = open(sys.argv[1],'r')
n = open('Updated'+sys.argv[1],'w')

lines = f.readlines()
f.close()

for line in lines:
	to_write = ''
	for i in line:
		if i == '_':
			to_write += ' '
		else:
			to_write += i
	to_write = to_write.lower().strip()
	n.write(to_write+'\n')
	print(to_write)

