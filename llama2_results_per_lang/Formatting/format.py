# this script is supposed to format the llama2 files so they can be evaluated
# Assumes that terms are written in only a few different ways

import sys

path = 'Formatted/'

to_format = sys.argv[1]
f = open(to_format,'r')
lines = f.readlines()
f.close()

n = open(path + 'FinalList' + to_format,'w')
count = 0
prev_num = 0
prev_star = 0
for line in lines:
    if line[0] == '*':
        prev_num = 0
        if prev_star < 10:
            if ':' in line:
                if line.count('"') >= 4:
                    sub = line[line.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    to_write = sub[:sub.index('"')]+'\n'
                else:
                    index = line.index(':')+2
                    to_write = line[index:]
            elif '-' in line:
                if line.count('"') >= 4:
                    sub = line[line.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    to_write = sub[:sub.index('"')]+'\n'
                else:
                    index = line.index('-')+2
                    to_write = line[index:]
            elif '=>' in line:
                if line.count('"') >= 4:
                    sub = line[line.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    to_write = sub[:sub.index('"')]+'\n'
                else:
                    index = line.index('>')+2
                    to_write = line[index:]
            elif '=' in line:
                if line.count('"') >= 4:
                    sub = line[line.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    to_write = sub[:sub.index('"')]+'\n'
                #elif line.count('"') == 2:
                #    sub = line[line.index('"')+1:]
                #    to_write = sub[:sub.index('"')]+'\n'
                else:
                    to_write = line[line.index('=')+2:]
            else:
                index = 2
                to_write = line[index:]
            n.write(to_write)
            count += 1
            prev_star += 1
            
            
    elif line[0].isdigit():
        prev_star = 0
        if prev_num < 10:
            prev_num += 1
            if ':' in line:
                if line.count('"') >= 4:
                    sub = line[line.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    to_write = sub[:sub.index('"')]+'\n'
                else:
                    index = line.index(':')+2
                    to_write = line[index:]
            elif '-' in line:
                if line.count('"') >= 4:
                    sub = line[line.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    to_write = sub[:sub.index('"')]+'\n'
                else:
                    index = line.index('-')+2
                    to_write = line[index:]
            elif '=>' in line:
                if line.count('"') >= 4:
                    sub = line[line.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    to_write = sub[:sub.index('"')]+'\n'
                else:
                    index = line.index('>')+2
                    to_write = line[index:]
            elif '=' in line:
                if line.count('"') >= 4:
                    sub = line[line.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    sub = sub[sub.index('"')+1:]
                    to_write = sub[:sub.index('"')]+'\n'
                else:
                    to_write = line[line.index('=')+2:]
            else:
                index = 3
                to_write = line[index:]
            n.write(to_write)
            count += 1
            prev_star += 1
    # this is for translations embedded in paragraph explanation
    elif line.count('"') == 4:
        prev_num = 0
        prev_star = 0
        sub = line[line.index('"')+1:]
        sub = sub[sub.index('"')+1:]
        sub = sub[sub.index('"')+1:]
        to_write = sub[:sub.index('"')]+'\n'
        n.write(to_write)
        count += 1
        
    else:
        prev_num = 0
        prev_star = 0

n.close()
print(count,'translated terms written')

    
