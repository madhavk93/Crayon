import nltk
wikiFile = open ('Unilever Wiki.txt', 'r')
posFile = open ('Unilever Wiki NNP.txt', 'w')

try:
    sentence = wikiFile.readlines()
        
except StopIteration as e:
    print "File is empty"

number = 0

for a in sentence:
    content = a.decode('utf-8')
    tokens = nltk.word_tokenize(content)
    tagged = nltk.pos_tag(tokens)

    for i in tagged:
        pos = i[1]
        if (pos == 'NNP' or pos == 'NNPS'):
            temp = i[0].encode ('utf-8')
            posFile.write (temp)
            posFile.write ('\n')                        
            number+=1            

z = str (number)            
posFile.write (z)

posFile.close()
wikiFile.close()
