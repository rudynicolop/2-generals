from time import sleep

def pause ():
    print ("...")
    input ("Press any key to continue.")
    print ("...")

print ("So, you would like to learn about the Two-Generals problem?")

pause ()

print ("A horde of Barbarians is marching to Rome, one of the cradles" \
    " of Western Civilization!")

pause ()

print ("Caesar has charged Generals A and B with the defense of Rome," \
    " each commanding a legion of soldiers.")

pause ()

print ("On the road to Rome, the Barbarians make camp between" \
    " two hills.")
print ("General A's division waits upon the left hill." \
    " General B's division waits upon the right hill.")

pause ()

print ("Combined, Generals A's and B's divisions would indoubitably vanquish" \
    " the Barbarian horde.")
print("However, individually, each division would meet" \
    " certain defeat to the Barbarians!")

pause ()

print ("Generals A and B must coordinate their attacks so that they strike" \
    " the Barbarian horde at the same, agreed upon time.")
print ("The only way Generals A and B can communicate between each other is via" \
    " messenger, who must sneak through the enemy camp to reach the other General.")
print ("The messenger is constantly in peril, and may be killed before reaching" \
    " the other General!")
print ("Can Generals A and B save Western Civilization?")

pause ()

sender = "A"
receiver = "B"

knows = "General {} knows to attack at dawn.".format(receiver)

article = "a"

msg = "message to attack at dawn"

while True:

    print ("General {} sends {} {} to General {}.".format(sender,article,msg,receiver))

    print ("Now, " + knows)

    that_knows = " that " + knows

    pause ()

    print ("But General {} doesn't know".format(sender) + that_knows)

    # Loop epilogue

    article = "an"

    msg = "acknowledgement message to the " + msg

    knows = "General {} knows".format(sender) + that_knows

    sender,receiver = receiver,sender

    pause ()
