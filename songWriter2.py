from random import randint
from rhyme import rhyme_finder
from nltk.tokenize import word_tokenize 
import markovify

def get_word(wf):
    count = 0;
    for key in wf:
        count+=wf[key]
    rand=randint(1,count)
    for key in wf:
        if(rand<=wf[key]):
            return key
        else:
            rand -= wf[key]

def syllable_count(word):
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
            if word.endswith("e"):
                count -= 1
    if count == 0:
        count += 1
    return count

def clean(str):
    punc = set([',','.','"','?','!','(',')'])
    if str[-1] in punc:
        return str[:-1]
    return str

def match_rhyme(stem, model,text):

    try:
        ls = rhyme_finder(stem, text)
    except KeyError:
        return None
    if not ls:
        return None

    for n in range(100):
        while True:
            rhyme_line = model.make_sentence() 

            if rhyme_line is not None:
                rhyme_stem = clean(rhyme_line.rsplit(None, 1)[-1])

                if rhyme_stem in ls:
                    return rhyme_line

                break


    return None

def make_chorus(model,text):
    
    print("making chorus")
    chorus = ''
    stem0 = None
    stem1 = None
    #ABAB rhyme
    line=None
    for i in range(4):
        #while line is None:

            if i == 2:
                match = match_rhyme(stem0, model,text)

                if match is not None:
                    chorus += (match + '\n')
                    break

            if i == 3:
                match = match_rhyme(stem1, model,text)

                if match is not None:
                    chorus += (match + '\n')
                    break

            line = model.make_sentence()


            if line is not None:

                if i == 0:
                    stem0 = clean(line.rsplit(None, 1)[-1])

                chorus += (line + '\n')
                break
            
                if i == 1:
                    stem1 = clean(line.rsplit(None, 1)[-1])

                chorus += (line + '\n')
                break

    return chorus

def make_verse(model,text):
    verse = ''
    for i in range(6):
        while True:
            line = model.make_sentence()
            print(line)
            if line is not None:
                print(line)
                verse += (line + '\n')
                
        print(verse)

    return verse

def main():
    f1=open ('lp.txt','r')
    f2=open('lp_tokenize.txt','w')
    for line in f1:
        tokens = word_tokenize(line)
        f2.write(' '.join(tokens))

    #Read the file
    with open('lp.txt','r') as f:
        text21=f.read().lower().split(' ')

    
    with open('lp_tokenize.txt','r') as f:
        text=f.read().lower().split(' ')

    model = markovify.NewlineText(text, state_size=1)  
    
    
    #Count frequency
    wordfreq={}
    for i in range(0,len(text)-1):
        word1=text[i]
        word2=text[i+1]
        if word1 not in wordfreq:
            wordfreq[word1]={}
        if word2 not in wordfreq[word1]:
            wordfreq[word1][word2]=1
        else:
            wordfreq[word1][word2]+=1

    song=""
    v1=make_verse(model,text)
    c=make_chorus(model,text)
    v2=make_verse(model,text)
    v3=make_verse(model,text)
    song=v1+"\n\n"+c+v2+"\n\n"+c+"\n\n"+v3+"\n\n"+c
    print(song)

if __name__=="__main__":
    main()










