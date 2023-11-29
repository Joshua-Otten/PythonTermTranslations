import sys

english = open('../../../Gold/unabbreviatedSplit.txt','r')
english_lines = english.readlines()
english.close()
trans = open(sys.argv[1],'r')
trans_lines = trans.readlines()
trans.close()

new = open('COMPARE'+sys.argv[1],'w')

for i in range(len(english_lines)):
	if i < len(trans_lines):
		new.write(english_lines[i].strip()+' : '+trans_lines[i].strip()+'\n')
	else:
		new.write(english_lines[i].strip()+' : \n')
new.close()

