# This code evaluates both a file of outputs, and a file of correct translations
# each file is formatted the same way a LanguageKey is formatted (each term on one line), but we don't have underscores, etc.  Formatting subject to change depending on how translators write output, etc
# We compare the lemmatized versions of the expanded terms
# if stanza does not support a particular language, we will have to evaluate that some other way
from torchmetrics.text import CHRFScore

def beginning_download(lang_id):
    import stanza
    #stanza.download(lang_id) # only needs to be done once per lang
    nlp = stanza.Pipeline(lang_id)
    print('completed initializations')
    return nlp

# creates a new file where all words are lemmatized
def lemmatize(file, nlp):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    
    docs = [stanza.Document([], text=line.strip()) for line in lines]
    
    out_docs = nlp(docs) # out_docs is a list
    
    # now write this to new files
    new = open('lemmatized_'+file,'w')
    for line in out_docs:
        for sentence in line.sentences:
            to_write = list()
            for word in sentence.words:
                to_write.append(word.lemma)
            new.write(' '.join(to_write).lower()+'\n')
            
    print('lemmatized:',file)



# this function compares two lemmatized files
def raw_accuracy(gold_trans, test_trans):
    # open and read the files
    gold_trans = open(gold_trans,'r')
    gold = gold_trans.readlines()
    gold_trans.close()
    test_trans = open(test_trans,'r')
    test = test_trans.readlines()
    test_trans.close()
    if len(gold) != len(test):
        print("Error: lengths of the two sets do not match")
        print("Length of golden set:",len(gold))
        print("Length of test:",len(test))
    correct = 0
    total = len(gold)
    for i in range(len(gold)):
        if gold[i].lower().strip() == test[i].lower().strip():
            correct += 1
    #print(f"\t{correct} correct out of {total}")
    print(f"\tRaw: {100*correct/total:.2f}%")



def CHRF_score(gold_trans, test_trans):
    chrf = CHRFScore()
    gold_trans = open(gold_trans,'r')
    gold = gold_trans.readlines()
    gold_trans.close()
    test_trans = open(test_trans,'r')
    test = test_trans.readlines()
    test_trans.close()
    if len(gold) != len(test):
        print("Error: lengths of the two sets do not match")
        print("Length of golden set:",len(gold))
        print("Length of test:",len(test))
    total = len(gold)
    all_scores = 0
    for i in range(len(gold)):
        target = [gold[i].lower().strip()]
        pred = [test[i].lower().strip()]
        score = chrf(pred, target).item()
        all_scores += score
    #print("Avg CHRF score is:",all_scores/total)
    print(f"\tCHRF: {100*all_scores/total:.2f}%")
        
def print_llm_scores(language, prompt):
    print('"'+language+'"')
    print('ChatGPT')
    raw_accuracy('Gold/'+language+'Key.txt','ChatGPT/'+language+prompt+'.txt')
    CHRF_score('Gold/'+language+'Key.txt','ChatGPT/'+language+prompt+'.txt')
    print('Llama2')
    raw_accuracy('Gold/'+language+'Key.txt','Llama2/'+language+prompt+'.txt')
    CHRF_score('Gold/'+language+'Key.txt','Llama2/'+language+prompt+'.txt')

def print_google_scores(language, version):
    print('"'+language+'"')
    raw_accuracy('Gold/'+language+'Key.txt','GoogleTranslate/'+language+version+'.txt')
    CHRF_score('Gold/'+language+'Key.txt','GoogleTranslate/'+language+version+'.txt')

# for testing
#nlp = beginning_download('fr')
#lemmatize('Llama2_zero_French.txt', nlp)
#lemmatize('FrenchKey.txt', nlp)

# in the function -> Gold first, then test file


print('Get warning message out of the way:')
CHRF_score('Gold/SpanishKey.txt','Llama2/Spanish_zero_shot_prompt.txt')
print('\n')


# Automatically evaluating all languages over raw accuracy + CHRF
test_languages = ['Spanish','French','Greek','Mandarin','Hindi','Bengali','Arabic','SoraniKurdish']

# ChatGPT and Llama2

prompts = ['_zero_shot_prompt','_zero_shot_motivation','_one_example','_few_shot','_entire_set_prompt']
for prompt in prompts:
    print('PROMPT:',prompt[1:])
    for language in test_languages:
        print_llm_scores(language,prompt)
        print()

# Google Translate
print('\nGOOGLE TRANSLATE SCORES\n')
versions = ['V1','V2','V3']
for version in versions:
    print('VERSION:',version)
    for language in test_languages:
        print_google_scores(language, version)
        print()
    print()

