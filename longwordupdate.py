def function():
    alice = open('alice.txt','r')
    alice_read = alice.read()
    y = '' ; long = ''
    letter = 0
    while alice_read:
        for x in alice_read:
            if ' ' in x or '\n' in x or ',' in x: #IF THERE IS A SPACE OR COMMA#
                y = ''       
            else:
                y = ('' +str(y)+ '' +str(x)+ '')   
            if (len(y)) > (len(long)):
                long = y #LONGEST WORD#
        break
    for x in long:
        letter += 1 #LENGTH#
    print(long) ; print(letter)

function()
#CWATTS#
#COMP PROG#
#3 7 18#
