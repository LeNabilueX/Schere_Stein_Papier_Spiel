import random
print("Spiele Schere-Stein-Papier mit mir")
print("Bitte wähle: Schere (s), Sein (r), Papier (p)")
eingabe = input("Deine Wahl: ")
spielzuege = ["s", "p", "r"]
if eingabe in spielzuege:
    random.shuffle(spielzuege)
    computer = spielzuege[0]
    import random
    if computer == eingabe:
        print("Unentschieden")
    if computer == "s" and eingabe == "p":
        print("Du hast verloren!")
    if computer =="s" and eingabe == "r":
        print("Du hast gewonnen!")
    if computer == "r" and eingabe == "p":
        print ("Du hast gewonnen!")
    if computer == "r" and eingabe == "s":
        print("Du hast verloren!")
    if computer == "p" and eingabe == "s":
        print("Du hast gewonnen!")
    if computer == "p" and eingabe == "r":
        print("Du hast verloren!")
else:
    print("Falsche Eingabe!")