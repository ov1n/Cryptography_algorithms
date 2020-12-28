def kamasutra(key,text):

    if(len(key)!=26):
        print("Please enter a valid key with 26 digits")

    keys1=[]
    keys2=[]
    out=[]

    #row generation
    for c in range(0,13):
        
        keys1.append(key[c])

    for c in range(13,26):
        
        keys2.append(key[c])

    print(keys1)
    print(keys2)

    for t in text:

        for i in range(0,13):
            if(keys1[i]==t):
                out.append(keys2[i])
            elif(keys2[i]==t):
                out.append(keys1[i])

    print(out)

kamasutra("abcdefghijklmnopqrstuvwxyz","abcd")
        
        
