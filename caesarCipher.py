def caesarCipher(mode,text,skip):

    #format plaintext
    text=text.upper()
    skip=skip%26

    #array for ciphertext
    cipher=""
    
    for c in text:
        if(c==' '):
            token=32
        else:
            #print(ord(c))
            if(mode):
                token=((ord(c)+skip)%91)
            else:
                token=(ord(c)-skip)
                #if it goes minus
                if(token<65):
                    token+=26
            #since ascii values are taken
            if(token<65):
                token+=65
                
        cipher+=chr(token)
            
    return(cipher)


chapter="It was dark and Merry could see nothing as he lay on the ground rolled in a blanket; yet though the night was airless and windless, all about him hidden trees were sighing softly. He lifted his head. Then he heard it again: a sound like faint drums in the wooded hills and mountain-steps. The throb would cease suddenly and then be taken up again at some other point, now nearer, now further off. He wondered if the watchmen had heard it.He could not see them, but he knew that all round him wer"

print(caesarCipher(1,"abcdefghijklmnopqrstuvwxyz",25))
print(caesarCipher(0,"ZABCDEFGHIJKLMNOPQRSTUVWXY",25))
