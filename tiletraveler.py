#gera föll fyrir hvern reit sem prentar út leiðbeiningarnar
#og biður um input um "direction" frá notendanum sem síðan
#fer í gegnum while lykkju sem inniheldur if og elif þar sem hann breytir
#staðfestingu leikmannsins í leiknum ef passar við annars fer hann í gegnum else
#setningu þar semhann prentar viðeigandi setningar og skilar leikmanni aftur í while lykkjuna og og hún runnar þartil
#hún fær viðeigandi gildi og svo koll af kolli.
#þegar leikmaður er kominn á reit 3 þá prentar forritið "Victory!" setninguna og while lykkjan stoppar

#1. mér fannst falla forritið einfaldlega einfaldara í uppsetningu og því fannst mér það þægilegra og skiljanlegra.
#2. Forritið sem inniheldur föll er mun skiljanlegra og lesanlegra.
#3. ég gat búið til fall fyrir hvern reit sem einfaldar mjög skilninginn á forritinu

def position_4():
    print("(N)orth or (E)ast or (S)outh.")
    new_position = input("Direction: ")
    while True:
        if new_position.upper() == "N":
            return 7
        elif new_position.upper() == "S":
            return 1
        elif new_position.upper() == "E":
            return 5
        else:
            print("Not a valid direction!")
            new_position = input("Direction: ")

def position_1():
    print("(N)orth.")
    new_position = input("Direction: ")
    while True:

        if new_position.upper() == "N":
            return 4
        else:
            print("Not a valid direction!")
            new_position = input("Direction: ")
           
def position_5():
    print("(S)outh or (W)est. ")
    new_position = input("Direction: ")
    while True:
        if new_position.upper() == "S":
            return 2
        elif new_position.upper() == "W":
            return 4
        else:
            print("Not a valid direction!")
            new_position = input("Direction: ")
    
def position_2():
    print("(N)orth. ")
    new_position = input("Direction: ")
    while True:
        if new_position.upper() == "N":
            return 5
        else:
            print("Not a valid direction!")
            new_position = input("Direction: ")

def position_7():
    print("(E)ast or (S)outh.")
    new_position = input("Direction: ")
    while True:
        if new_position.upper() == "S":
            return 4
        elif new_position.upper() == "E":
            return 8
        else:
            print("Not a valid direction!")
            new_position = input("Direction: ")

def position_8():
    print("(E)ast or (W)est.")
    new_position = input("Direction: ")
    while True:
        if new_position.upper() == "E":
            return 9
        elif new_position.upper() == "W":
            return 7
        else:
            print("Not a valid direction!")
            new_position = input("Direction: ")

def position_9():
    print("(S)outh or (W)est.")
    new_position = input("Direction: ")
    while True:
        if new_position.upper() == "S":
            return 6
        elif new_position.upper() == "W":
            return 8
        else:
            print("Not a valid direction!")
            new_position = input("Direction: ")

def position_6():
    print("(N)orth or (S)outh.")
    new_position = input("Direction: ")
    while True:
        if new_position.upper() == "N":
            return 9
        elif new_position.upper() == "S":
            return 3
        else:
            print("Not a valid direction!")
            new_position = input("Direction: ")



position = 1

while position != 3:
    print("You can travel: " , end="")
    
    if position == 4:
        position = position_4()

    elif position == 1:
        position = position_1()

    elif position == 5:
        position = position_5()

    elif position == 2:
        position = position_2()

    elif position == 7:
        position = position_7()
        
    elif position == 8:
        position = position_8()

    elif position == 9:
        position = position_9()

    elif position == 6:
        position = position_6()
        

print("Victory!")