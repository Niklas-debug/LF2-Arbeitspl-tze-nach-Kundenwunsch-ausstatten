# Import zweier notwendigen Bibliotheken.
import sys #Diese Bibliothek ermöglicht den Zugriff auf einige Variablen, die von Python verwendet oder verwaltet werden.
import time #Diese Bibliothek bietet verschiedene Funktionen für die Zeit.

#Methode um einen Vorgang im Programm abzubrechen.
def abbruch():
    print('\nDer Prozess wurde abgebrochen!')
    exit(1) #Parameter "1" in der exit() Funktion dient zur darstellung eines Fehlers da das Programm an dieser Stelle absichtlich abgebrochen wurde,


#Liste zur deklarierung/defenierung wie viele Sekunden eine Sekunde, Minute oder Stunde hat.
intervals = (
    ('Stunden', 3600),
    ('Minuten', 60),
    ('Sekunden', 1)
)


#Methode zur vereinfachten und wörtlichen darstellung der Zeit die bereits abgelaufen ist.
def zeit_anzeigen(sekunden, abrundung=2):
    ergebniss = []

    for name, zaehler in intervals:
        wert = sekunden // zaehler
        if wert:
            sekunden -= wert * zaehler
            if wert == 1:
                name = name.rstrip('n')
            ergebniss.append("{} {}".format(wert, name))
    return ', '.join(ergebniss[:abrundung])


#Methode zur kalkulation und ausgabe der Fahrzeit oder Nutzungsdauer
def kalkulation(zeit):
    berechneteZeit = zeit / 60
    ergeniss = 1 + berechneteZeit * 0.2
    rundung = round(ergeniss, 2)
    print(f"\rDer Preis für diese Fahrt beträgt: {rundung}€")


#Methode zum Zählen der vergangenden Zeit seit beginn der Nutzung. Gibt ebenfalls die abgelaufdene Zeit in der Konsole platzsparend aus.
def zaehler():
    try:
        print("Drücke STRG + C zum abbrechen der Nutzung.")
        for i in range(0, 3600, +1):
            zeit = zeit_anzeigen(i)
            sys.stdout.write(f"\rAbgelaufene Zeit: {zeit}")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt: #Erlaubt das abbrechen über STRG + C um selber zu entscheiden was danach passiert.
        sys.stdout.flush()
        print(f"\nDie Fahr wurde abgebrochen!")
    finally:
        sys.stdout.write('\n')
        kalkulation(i)


#Zeigt die Preisübersicht an. Hier entscheidet man ebenfalls ob man die Fahrt starten will oder nicht.
def preisUebersicht():
    try:
        while True:
            print('\nDie Grundgebühr beträgt 1€.\nEine Minute kostet 0,20€\nDie Maximale Nutzungsdauer beträgt 1 Stunde.\n')
            x = input('Wenn du die Tour starten willst, drücke [Enter]!')
            y = input('Bist du dir sicher das du starten willst? Drücke [J] für Ja und [N] für nein:\n')
            if y == 'j' or y == 'J':
                zaehler()
                break
            elif y == 'n' or y == 'N':
                print('Der Prozess wurde abgebrochen! Dir werden keine Kosten berechnet.')
                break
                exit(0)
            else:
                print('Du sollst [J] für Ja und [N] für Nein drücken:\n')
    except KeyboardInterrupt: #Erlaubt das abbrechen über STRG + C um selber zu entscheiden was danach passiert.
        abbruch()


#Zeigt die Startseite an.
def intro():
    try:
        x = input('Wilkommen bei ScooTeq! Drücke [Enter] wenn du fortfahren willst!')
        preisUebersicht()
    except KeyboardInterrupt: #Erlaubt das abbrechen über STRG + C um selber zu entscheiden was danach passiert.
        abbruch()

#Führt das Programm aus nachdem alle Methoden defeniert wurden.
if __name__ == '__main__':
    intro()