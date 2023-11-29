# this script is supposed to format the files so they can be evaluated
# assumes translated terms are written in only a few different ways
# args: [to_format]
import sys

path = 'Formatted/FinalList'

to_format = sys.argv[1]
f = open(to_format,'r')
lines = f.readlines()
f.close()

n = open(path + to_format,'w') # new formatted-to-be file
translations = set()
count = 0
prev_colon = 0
prev_hyphen = 0
prev_arrow = 0
for line in lines:
    if line[0] == ',' or line[0] == '.' or len(line) < 2:
        prev_colon = 0
        prev_hyphen = 0
        prev_arrow = 0
    elif ',' in line or '，' in line or '،' in line:
        # assume that this is a list of translated terms, separated by commas
        prev_colon = 0
        prev_hyphen = 0
        prev_arrow = 0
        if ',' in line:
            terms = line.split(', ')[:10] # only the first 10
        elif '،' in line:
            terms = line.split('،')[:10]
        else:
            terms = line.split('，')[:10]
        for term in terms:
            if term[len(term)-1] == '\n': # end of sentence period
                if term[len(term)-2]=='.':
                    to_write = term[:len(term)-2].lower().strip()
                else:
                    to_write = term[:len(term)-1].lower().strip()
            else:
                to_write = term.lower().strip()
            if to_write != '':#True:#to_write not in translations:
                n.write(to_write+'\n')
                print(':'+to_write+':')
                translations.add(to_write)
                count += 1
            
            
    elif ':' in line or '：' in line:
        # assume that this is one translated term on the right, English on the left
        prev_hyphen = 0
        prev_arrow = 0
        if ':' in line:
            index = line.index(':')+2
        else:
            index = line.index('：')+2
        to_write = line.lower().strip()
        if prev_colon < 10 and to_write != '':#True:#to_write not in translations:
            n.write(to_write+'\n')
            print(':'+to_write+':')
            translations.add(to_write)
            count += 1
            prev_colon += 1

    elif False:#'-' in line:
        # assume this is one translated term on the right, English on the left
        prev_colon = 0
        prev_arrow = 0
        index = line.index('-')+2
        to_write = line[index:].lower().strip()
        if prev_hyphen < 10 and to_write != '':#True:#to_write not in translations:
            n.write(to_write+'\n')
            print(':'+to_write+':')
            translations.add(to_write)
            count += 1
            prev_hyphen += 1
    elif '=>' in line:
        # assume this is one translated term on the right, English on the left
        prev_colon = 0
        prev_hyphen = 0
        index = line.index('>')+2
        to_write = line.lower().strip()
        if prev_arrow < 10 and to_write != '':#True:#to_write not in translations:
            n.write(to_write+'\n')
            print(':'+to_write+':')
            translations.add(to_write)
            count += 1
            prev_arrow += 1
    else:
        print('UNEXPECTED LINE / No : , or -')
        print(line)

n.close()
print(count,'translated terms written')
