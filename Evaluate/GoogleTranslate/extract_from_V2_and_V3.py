
# do this for French, Greek, Hindi, Bengali, and Mandarin

print('V2')

f = open('FrenchWholeV2.txt','r')
lines = f.readlines()
f.close()
n = open('FrenchV2.txt','w')
print('French')

for line in lines:
    if ':' in line:
        # we want everything before the colon
        to_write = line[:line.index(':')].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line

    n.write(to_write+'\n')

n.close()


f = open('GreekWholeV2.txt','r')
lines = f.readlines()
f.close()
n = open('GreekV2.txt','w')
print('Greek')

for line in lines:
    if ':' in line:
        # we want everything before the colon
        to_write = line[:line.index(':')].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line

    n.write(to_write+'\n')

n.close()

f = open('HindiWholeV2.txt','r')
lines = f.readlines()
f.close()
n = open('HindiV2.txt','w')
print('Hindi')

for line in lines:
    if ':' in line:
        # we want everything before the colon
        to_write = line[:line.index(':')].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line

    n.write(to_write+'\n')

n.close()

f = open('BengaliWholeV2.txt','r')
lines = f.readlines()
f.close()
n = open('BengaliV2.txt','w')
print('Bengali')

for line in lines:
    if ':' in line:
        # we want everything before the colon
        to_write = line[:line.index(':')].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line

    n.write(to_write+'\n')

n.close()

f = open('MandarinWholeV2.txt','r')
lines = f.readlines()
f.close()
n = open('MandarinV2.txt','w')
print('Mandarin')

for line in lines:
    if '：' in line:
        # we want everything before the colon
        to_write = line[:line.index('：')].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line
    n.write(to_write+'\n')

n.close()

f = open('SoraniKurdishWholeV2.txt','r')
lines = f.readlines()
f.close()
n = open('SoraniKurdishV2.txt','w')
print('Sorani Kurdish')

for line in lines:
    if ':' in line:
        # we want everything before the colon
        to_write = line[:line.index(':')].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line

    n.write(to_write+'\n')

n.close()


#### V3 ####
print('NOW FOR V3')

f = open('FrenchWholeV3.txt','r')
lines = f.readlines()
f.close()
n = open('FrenchV3.txt','w')
print('French')

for line in lines:
    if ':' in line:
        # we want everything before the colon
        to_write = line[line.index(':')+1:].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line
    if to_write[len(to_write)-1] == '.':
        to_write = to_write[:len(to_write)-1]
    n.write(to_write+'\n')

n.close()


f = open('GreekWholeV3.txt','r')
lines = f.readlines()
f.close()
n = open('GreekV3.txt','w')
print('Greek')

for line in lines:
    if ':' in line:
        # we want everything before the colon
        to_write = line[line.index(':')+1:].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line
    if to_write[len(to_write)-1] == '.':
        to_write = to_write[:len(to_write)-1]
    n.write(to_write+'\n')

n.close()

f = open('HindiWholeV3.txt','r')
lines = f.readlines()
f.close()
n = open('HindiV3.txt','w')
print('Hindi')

for line in lines:
    if ':' in line:
        # we want everything before the colon
        to_write = line[line.index(':')+1:].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line
    if to_write[len(to_write)-1] == '।':
        to_write = to_write[:len(to_write)-1]
    n.write(to_write+'\n')

n.close()

f = open('BengaliWholeV3.txt','r')
lines = f.readlines()
f.close()
n = open('BengaliV3.txt','w')
print('Bengali')

for line in lines:
    if ':' in line:
        # we want everything before the colon
        to_write = line[line.index(':')+1:].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line
    if to_write[len(to_write)-1] == '।':
        to_write = to_write[:len(to_write)-1]
    n.write(to_write+'\n')

n.close()

f = open('MandarinWholeV3.txt','r')
lines = f.readlines()
f.close()
n = open('MandarinV3.txt','w')
print('Mandarin')
for line in lines:
    if '：' in line:
        # we want everything before the colon
        to_write = line[line.index('：')+1:].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line
    if to_write[len(to_write)-1] == '。':
        to_write = to_write[:len(to_write)-1]
    n.write(to_write+'\n')

n.close()


f = open('SoraniKurdishWholeV3.txt','r')
lines = f.readlines()
f.close()
n = open('SoraniKurdishV3.txt','w')
print('Sorani Kurdish')

for line in lines:
    if ':' in line:
        # we want everything before the colon
        to_write = line[line.index(':')+1:].lower().strip()
    else:
        print('Issue: no colon found!')
        to_write = line
    if to_write[len(to_write)-1] == '.':
        to_write = to_write[:len(to_write)-1]
    n.write(to_write+'\n')

n.close()
