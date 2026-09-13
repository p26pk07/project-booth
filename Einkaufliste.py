einkaufsliste =  [] 

print(" ")
print("Willkommen zur Einkaufliste")
print (" ")
print("----Menu----")
print("1. Artikel Hinzufügen")
print("2. letzten Artikel Löschen")
print("3. Liste ansehen ")
print("4. Beenden")
print("---------")
print(" ")
status = True

while status == True:
    inp = input("Welche Aktion möchtest du ausführen?(1,2,3 oder 4) -> ")
    


    def aritkel_hinzufuegen(artikel):
        einkaufsliste.append(artikel)
        print (f"{artikel} wurde zur Einkaufsliste hinzugefügt.")
        print (einkaufsliste)
    

    
    def artikel_entfernen():
        print(einkaufsliste)
        löschen = input("welchen Artikel möchtest du entfernen? -> ")

        if löschen in einkaufsliste:
            einkaufsliste.remove(löschen)
            print(" ")
            print(f"Der Artikel {löschen} wurde erfogreich entfernt")
        else:
            print("Der Artikel ist nicht in der Liste, versuche es erneut!")
        print(einkaufsliste)
        return einkaufsliste



    

    if inp == "1":
        input_artikel = input("Welchen Artikel möchtest du hinzufügen? -> ")
        aritkel_hinzufuegen(input_artikel)
   

    elif inp == "2":
        artikel_entfernen()
    

    elif inp == "3":
        print("EINKAUFSLISTE")
        print(einkaufsliste)
    

    elif inp == "4":
        print("Einkaufsliste wird geschlossen...")
        status = False
    else:
        print("Angabe nicht erkannt, versuche erneut")
    
   







