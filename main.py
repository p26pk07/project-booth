# ticket Preise ermitteln 
# unter 12 jahren kostenloszwischen 12 und 18 5€ und ü.18 7€
#schüler kriegen einen 10% rabbatt 
# studenten 15%

Name = input(f"Hallo gebe bitte deinen Namen ein -> ")
alter = int(input(f"Und wie alt bist du? -> "))
if input(f"Gehst du noch zur schule? -> ") == "ja" or "Ja":
  schueler = True
  
if schueler == True:
  student = False
else:
  input(f"Bist du student -> ") == "ja" or "Ja"
  student = True

preis = 5
preis_rabatt = 1
print("_______")
print(" ")
print(f"Hallo {Name}, da du {alter} jahre alt bist: ")
#rechner 
if alter < 12:
  preis = 0
elif alter >= 12 and alter < 18:
  preis = 5
else:
  preis = 7

if schueler == True:
 preis_rabatt = preis * 0.1 
 betrag  = preis - preis_rabatt
 print (f"kostet dein Ticket {betrag}€, nach abzug des Schülerrabattes")
elif schueler != True and student == True:
  preis_rabatt = preis * 0.15
  betrag = preis - preis_rabatt
  print(f"kostet dein Ticket {betrag}€, nach Abzug des Studentenrabatts")
else: 
  print(f"kostet dein Ticket {preis}")
