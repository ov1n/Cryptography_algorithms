##This algorithm simply replaces each character with
##a character in the same alphabet

import random

def simpleSubstitution(text,key=None):
    # if no parameter given , it means encrypt
    text=text.upper()
    message=""
    
    if(not(key)):
        cipher=random.sample(range(26),26)

        for i in text:

            if(i==" "):
                message.append(" ")
            else:
                
                for j in range(0,26):
            
                    if(ord((i))==j+65):
                        
                        message+=(chr(cipher[j]+65))
                        break
                    
    #if parameter given it is a decryption
    else:
        if(len(key)!=26):
            raise Exception("Key not equal to 26 characters")

        key=key.upper()
        cipher=[]

        #vectorize the key
        for c in key:
            cipher.append(ord(c)-65)

        for t in text:
            for j in range(0,26):
                if(t==key[j]):
                    print(chr(j+65),end="")
    return(message)

#encrypt with random key
print(simpleSubstitution("abcdefghijklmnopqrstuvwxyz"))

#decrypt with given key
print(simpleSubstitution("az","qwertyuiopasdfghjklzxcvbnm"))
    
    
