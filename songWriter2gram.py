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
    for i in range(0,len(text)-1):
        word1=text[i]
        word2=text[i+1]
        if word1 not in wordfreq:
            wordfreq[word1]={}
        if word2 not in wordfreq[word1]:
            wordfreq[word1][word2]=1
        else:
            wordfreq[word1][word2]+=1

    sentence=""
    t=randint(0,len(wordfreq.keys()))
    word=list(wordfreq.keys())[t]
    for i in range(200):
        sentence += word + " ";
        word=get_word(wordfreq[word])
    print(sentence)

if __name__=="__main__":
    main()










