import re

counter ={}
# define punctuation
punctuations = "._-()"
with open('declaration.txt','r') as file: 
    # reading each line     
    for line in file: 
        line = re.sub(r'[^\w\s]', '', line)
        line = line.lower()
        # reading each word   
        for word in line.split(): 
            # displaying the words            
            if(word in counter):
                counter[word] += 1
            else:
                if('-' in word or '.' in word or ',' in word):
                    word = word[-1]
                counter.update( {word : 1} )
sortedDict = dict( sorted(counter.items(), key=lambda x: x[0].lower()) )

f = open("declarationKey2.txt", "w")
for keys,values in sortedDict.items():
    f.write('{} {}'.format(keys,values))
    f.write('\n')

f.close() 
print(counter)

