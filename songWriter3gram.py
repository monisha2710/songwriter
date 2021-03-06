from random import randint

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

def main():
    #Read the file
    with open('21pilots.txt','r') as f:
        text=f.read().lower().split(' ')

    #Count frequency
    wordfreq={}
    for i in range(0,len(text)-2):
        word1=text[i]
        word2=text[i+1]
        word3=text[i+2]
        if word1 not in wordfreq:
            wordfreq[word1]={}
        if word2 not in wordfreq[word1]:
            wordfreq[word1][word2]={}
        if word3 not in wordfreq[word1][word2]:
            wordfreq[word1][word2][word3]=1
        else:
            wordfreq[word1][word2][word3]+=1

    word1=list(wordfreq.keys())[0]
    word2=list(wordfreq[word1].keys())[0]
    sentence = word1+" "+word2
    for i in range(200):
        word3 = get_word(wordfreq[word1][word2])
        sentence += word3 + " ";
        word1 = word2
        word2 = word3
        
    print(sentence)

if __name__=="__main__":
    main()










