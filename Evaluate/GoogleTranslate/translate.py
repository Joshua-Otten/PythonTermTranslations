# To install googletrans:
# pip install googletrans==4.0.0-rc1

# This code translates V2 and V3 into certain languages we did not have data for

import googletrans
from googletrans import Translator
translator = Translator()

# first V2
eng = open('EnglishTermsV2.txt','r')
eng_lines = eng.readlines()
eng.close()

'''
# Spanish
n = open('SpanishV2.txt','w')
for line in eng_lines:
    translation = translator.translate(line.strip(), src='en',dest='es').text
    if ':' in translation:
        # we want everything before the colon
        to_write = translation[:translation.index(':')].lower().strip()
    else:
        print('Issue!  No colon found')
        to_write = translation.lower().strip()
    n.write(to_write+'\n')
    print(to_write)

'''
# Arabic
n = open('ArabicV2.txt','w')
for line in eng_lines:
    translation = translator.translate(line.strip(), src='en',dest='ar').text
    if ':' in translation:
        # we want everything before the colon
        to_write = translation[:translation.index(':')].lower().strip()
    else:
        print('Issue!  No colon found')
        to_write = translation.lower().strip()
    n.write(to_write+'\n')
    print(to_write)
'''
# Kurdish
n = open('KurdishV2.txt','w')
for line in eng_lines:
    translation = translator.translate(line.strip(), src='en',dest='ku').text
    if ':' in translation:
        # we want everything before the colon
        to_write = translation[:translation.index(':')].lower().strip()
    else:
        print('Issue!  No colon found')
        to_write = translation.lower().strip()
    n.write(to_write+'\n')
    print(to_write)

 '''
### Now V3 ###
eng = open('EnglishTermsV3.txt','r')
eng_lines = eng.readlines()
eng.close()
'''
# Spanish
n = open('SpanishV3.txt','w')
for line in eng_lines:
    translation = translator.translate(line.strip(), src='en',dest='es').text
    if ':' in translation:
        # we want everything after the colon
        to_write = translation[translation.index(':')+1:].lower().strip()
    else:
        print('Issue!  No colon found')
        to_write = translation
    n.write(to_write+'\n')
    print(to_write)

# Arabic
n = open('ArabicV3.txt','w')
for line in eng_lines:
    translation = translator.translate(line.strip(), src='en',dest='ar').text
    if ':' in translation:
        # we want everything after the colon
        to_write = translation[translation.index(':')+1:].lower().strip()
    else:
        print('Issue!  No colon found')
        to_write = translation
    n.write(to_write+'\n')
    print(to_write)
'''
# Kurdish
n = open('KurdishV3.txt','w')
for line in eng_lines:
    translation = translator.translate(line.strip(), src='en',dest='ku').text
    if ':' in translation:
        # we want everything after the colon
        to_write = translation[translation.index(':')+1:].lower().strip()
    else:
        print('Issue!  No colon found')
        to_write = translation
    n.write(to_write+'\n')
    print(to_write)
