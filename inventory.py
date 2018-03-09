def function():
    inv = {'apple':5 , 'kiwi':900 , 'banana':20 , 'lemon':100} #has fruits and values and stuff#
    while True:
        item = input(">> What fruit would you like to remove?").lower() ; print ("") #wat fruit they wanna remove#
        if item in inv:
            remove = +int(input(">> How many would you like to remove?")) ; inv[item] = inv[item] - (remove) #how many they remove#
            if inv[item] < 0: #if its less than 0, there is now 0 of that fruit left. Because its impossible to have a - amount of fruits irl, and im going for realism.
                inv[item] = 0
            print ("\n> You now have " +str(inv[item])+ " " +str(item)+ "s.\n")
        else:
            print ('> Unknown fruit "' +str(item)+ '"\n') #if they are stupid, and cant read#
function()
