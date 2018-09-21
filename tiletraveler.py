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

position = 1

while position != 3:
    print("You can travel: " , end="")
    if position == 4:
        print("(N)orth or (E)ast or (S)outh.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "N":
                position = 7
                break
            elif new_position.upper() == "S":
                position = 1
                break
            elif new_position.upper() == "E":
                position = 5
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")
    elif position == 1:
        print("(N)orth.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "N":
                position = 4
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")
    elif position == 5:
        print("(S)outh or (W)est. ")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "S":
                position = 2
                break
            elif new_position.upper() == "W":
                position = 4
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")

    elif position == 2:
        print("(N)orth. ")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "N":
                position = 5
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")

    elif position == 7:
        print("(E)ast or (S)outh.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "S":
                position = 4
                break
            elif new_position.upper() == "E":
                position = 8
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")

    elif position == 8:
        print("(E)ast or (W)est.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "E":
                position = 9
                break
            elif new_position.upper() == "W":
                position = 7
                break
            else:
                print("Not a valid direction!")
                ew_position = input("Direction: ")

    elif position == 9:
        print("(S)outh or (W)est.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "S":
                position = 6
                break
            elif new_position.upper() == "W":
                position = 8
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")

    elif position == 6:
        print("(N)orth or (S)outh.")
        new_position = input("Direction: ")
        while True:
            if new_position.upper() == "N":
                position = 9
                break
            elif new_position.upper() == "S":
                position = 3
                break
            else:
                print("Not a valid direction!")
                new_position = input("Direction: ")

print("Victory!")
