# args: [path + file to reformat] [path + new name]
# this code will likely need to change depending on the input file, so it will be a work-in-progress
import sys

f = open(sys.argv[1],'r')
lines = f.readlines()
f.close()

n = open(sys.argv[2],'w')
count = 0
for line in lines:
    line = line.strip()
    # if Chinese starts with 、
    if len(line) > 1 and line[0] == '、':
        line = line[1:]
    # if "term" is "translation"
    if line.count('"') >= 4:
        sub = line[line.index('"')+1:]
        sub = sub[sub.index('"')+1:]
        sub = sub[sub.index('"')+1:]
        to_write = sub[:sub.index('"')]+'\n'
    # if translation is surrounded by "double quotes"
    elif len(line) > 1 and line[0] == '"' and line[len(line)-1] == '"':
        to_write = line[1:len(line)-1]
    # if term: translation
    elif ':' in line:
        to_write = line[line.index(':')+2:]
    elif '：' in line:
        to_write = line[line.index('：')+2:]
    # if term => translation
    elif '=>' in line:
        to_write = line[line.index('>')+2:]
    # if term - translation
    elif ' - ' in line:
        to_write = line[line.index('-')+2:]
    # if term = translation
    elif ' = ' in line:
        to_write = line[line.index('=')+2:]
    # if term -> translation
    elif '->' in line:
        to_write = line[line.index('>')+2:]
    # if something in parentheses
    # some words are only given as (pronunciation)--this is not good enough anyway
    elif '(' in line and ')' in line:
        to_write = line[:line.index('(')]
        if len(to_write) < 1:
            to_write = '-' # meaning no translation essentially
    # same as above but with slightly different characters
    elif '（' in line and '）' in line:
        to_write = line[:line.index('（')]
        if len(to_write) < 1:
            to_write = '-' # meaning no translation essentially
    # if term (translation
    elif '(' in line:
        to_write = line[line.index('(')+1:]
    # same as above but with slightly different character
    elif '（' in line:
        to_write = line[line.index('（')+1:]
      
    else:
        to_write = line
    
    
    to_write = to_write.lower().strip()
    
    # if , or . or 。 at end of line
    if len(to_write) > 1 and (to_write[len(to_write)-1]==',' or to_write[len(to_write)-1]=='.' or to_write[len(to_write)-1]=='。' or to_write[len(to_write)-1]=='।'):
        to_write = to_write.strip()[:len(to_write.strip())-1]
    # replace underscores with spaces (to be consistent)
    if '_' in to_write:
        new = ''
        for char in to_write:
            if char == '_':
                new += ' '
            else:
                new += char
        to_write = new
    if len(to_write) < 1:
        to_write = '-'
    # done with all checks!
    n.write(to_write+'\n')
    count += 1
    print(to_write)
    
print(count)
