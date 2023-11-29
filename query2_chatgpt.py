# -*- coding: utf-8 -*-

import openai

openai.api_key = "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"
model_engine = "text-davinci-003" # use turbo
path = 'chatgpt_results_per_lang/'


# acquire the English list to translate
eng = open('Gold/unabbreviatedSplit.txt','r')
eng_terms = eng.readlines()
eng.close()
for i in range(len(eng_terms)):
    eng_terms[i] = eng_terms[i].strip()
'''
# Spanish
language = 'Spanish'

zero_shot_prompt = "Please translate these terms into "+language+": "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating these terms into "+language+": "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => valor absoluto.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => valor absoluto, memory view => vista de la memoria, power => elevar, print => imprimir, Syntax Error => Error de sintaxis.  Please translate these terms into "+language+": "

# give entire set for one language (French), translate to all the others
French_set_file = open('trans_examples_French.txt','r')
French_set = French_set_file.readline()
French_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to French, you have: " + French_set + ".  Please translate these terms into "+language+": "

#prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
prompts = [few_shot, entire_set_prompt]
#files = [language+'_zero_shot_prompt', language+'_zero_shot_motivation', language+'_one_example', language+'_few_shot', language+'_entire_set_prompt']
files = ['few_shot','entire_set_prompt']

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    k += 1
    # for every 10 terms, ask model to translate
    for i in range(0,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt+terms,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output = completion.choices[0].text
        print(output)
        f.write(output+'\n')
        
    f.close()

##################################
print('NOW ON TO FRENCH')
# French
language = 'French'

zero_shot_prompt = "Please translate these terms into "+language+": "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating these terms into "+language+": "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => valeur absolue.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => valeur absolue, memory view => mémoire visuelle, power => puissance, print => imprimer, Syntax Error => Erreur de syntaxe.  Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have: " + Spanish_set + ".  Please translate these terms into "+language+": "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = [language+'_zero_shot_prompt', language+'_zero_shot_motivation', language+'_one_example', language+'_few_shot', language+'_entire_set_prompt']

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    k += 1
    # for every 10 terms, ask model to translate
    for i in range(0,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt+terms,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output = completion.choices[0].text
        print(output)
        f.write(output+'\n')
        
    f.close()
'''
##################################
# Greek
print('NOW ON TO GREEK')
language = 'Greek'

zero_shot_prompt = "Please translate these terms into "+language+": "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating these terms into "+language+": "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => απόλ.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => απόλ, memory view => προβολή μνήμης, power => δύναμη, print => τύπωσε, Syntax Error => Συντακτικό λάθος.  Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have: " + Spanish_set + ".  Please translate these terms into "+language+": "

#prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
#files = [language+'_zero_shot_prompt', language+'_zero_shot_motivation', language+'_one_example', language+'_few_shot', language+'_entire_set_prompt']
prompts = [zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = [language+'_zero_shot_motivation', language+'_one_example', language+'_few_shot', language+'_entire_set_prompt']

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    k += 1
    if k==1:
        j = 65
    else:
        j = 0
    # for every 10 terms, ask model to translate
    for i in range(j,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt+terms,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output = completion.choices[0].text
        print(output)
        f.write(output+'\n')
    f.close()

##################################
# Mandarin
print('NOW ON TO MANDARIN')
language = 'Mandarin'

zero_shot_prompt = "Please translate these terms into "+language+": "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating these terms into "+language+": "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => 绝对值.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => 绝对值, memory view => 内存视图, power => 次方, print => 打印, Syntax Error => 语法错误.  Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have: " + Spanish_set + ".  Please translate these terms into "+language+": "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = [language+'_zero_shot_prompt', language+'_zero_shot_motivation', language+'_one_example', language+'_few_shot', language+'_entire_set_prompt']

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    k += 1
    # for every 10 terms, ask model to translate
    for i in range(0,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt+terms,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output = completion.choices[0].text
        print(output)
        f.write(output+'\n')
        
    f.close()

##################################
# Hindi
print('NOW ON TO HINDI')
language = 'Hindi'

zero_shot_prompt = "Please translate these terms into "+language+": "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating these terms into "+language+": "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => निरपेक्ष मान.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => निरपेक्ष मान, memory view => स्मृति_दर्शन, power => घात, print => प्रिंट, Syntax Error => वाक्यविन्यास त्रुटि.  Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have: " + Spanish_set + ".  Please translate these terms into "+language+": "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = [language+'_zero_shot_prompt', language+'_zero_shot_motivation', language+'_one_example', language+'_few_shot', language+'_entire_set_prompt']

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    k += 1
    # for every 10 terms, ask model to translate
    for i in range(0,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt+terms,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output = completion.choices[0].text
        print(output)
        f.write(output+'\n')
    f.close()
    
    
##################################
# Bengali
print('NOW ON TO BENGALI')
language = 'Bengali'

zero_shot_prompt = "Please translate these terms into "+language+": "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating these terms into "+language+": "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => निरपेक्ष मान.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => निरपेक्ष मान, memory view => स्मृति_दर्शन, power => घात, print => प्रिंट, Syntax Error => বাক্যগঠন ত্রুটি.  Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have: " + Spanish_set + ".  Please translate these terms into "+language+": "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = [language+'_zero_shot_prompt', language+'_zero_shot_motivation', language+'_one_example', language+'_few_shot', language+'_entire_set_prompt']

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    k += 1
    # for every 10 terms, ask model to translate
    for i in range(0,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt+terms,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output = completion.choices[0].text
        print(output)
        f.write(output+'\n')
    f.close()


##################################
# Sorani Kurdish
print('NOW ON TO SORANI KURDISH')
language = 'Sorani Kurdish'

zero_shot_prompt = "Please translate these terms into "+language+": "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating these terms into "+language+": "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => بەهای ڕەها.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => بەهای ڕەها, memory view => دیمەنی بیرگە, power => هێز, print => چاپکردن, Syntax Error => هەڵەی ڕستەسازی.  Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have: " + Spanish_set + ".  Please translate these terms into "+language+": "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = [language+'_zero_shot_prompt', language+'_zero_shot_motivation', language+'_one_example', language+'_few_shot', language+'_entire_set_prompt']

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    k += 1
    # for every 10 terms, ask model to translate
    for i in range(0,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt+terms,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output = completion.choices[0].text
        print(output)
        f.write(output+'\n')
        
    f.close()

##################################
# Arabic
print('NOW ON TO ARABIC')
language = 'Arabic'

zero_shot_prompt = "Please translate these terms into "+language+": "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating these terms into "+language+": "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => قيمة مطلقة.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example: absolute value => قيمة مطلقة, memory view => عرض الذاكرة, power => قوة, print => طباعة, Syntax Error => خطأ لغوي. Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have: " + Spanish_set + ".  Please translate these terms into "+language+": "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = [language+'_zero_shot_prompt', language+'_zero_shot_motivation', language+'_one_example', language+'_few_shot', language+'_entire_set_prompt']

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    k += 1
    # for every 10 terms, ask model to translate
    for i in range(0,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt+terms,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output = completion.choices[0].text
        print(output)
        f.write(output+'\n')
        
    f.close()

