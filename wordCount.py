import re

def store(counter):
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
                    counter.update( {word : 1} )
    return counter


def write(counter):
    #sorting the dict
    sortedDict = dict( sorted(counter.items(), key=lambda x: x[0].lower()) )
    #creating the file
    f = open("declarationKey2.txt", "w")
    #trasverse and write
    for keys,values in sortedDict.items():
        f.write('{} {}'.format(keys,values))
        f.write('\n')
    f.close() 
    #done
    print("done!"+'\n')
    
counter ={}
counter = store(counter)
write(counter)
