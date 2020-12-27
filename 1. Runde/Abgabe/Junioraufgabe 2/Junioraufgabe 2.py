#!/usr/bin/python

# Folgende Annahmen wurden genommen:
# -In dem Hauptverzeichnis liegt mindestens eine Datei, utf-8 encodiert, in der beide Karten liegen
# -Die Karten sind mit einem Zeilenumbruch voneinander getrennt
# -Die Karten enthalten  gleichviele Elemente
# -Die einzelnen Elemente sind mit " " voneinander getrennt
# -Es gibt eine mögliche Lösung

print("Junioraufgabe 2")


                                                    # Auslese der Datei mit beiden Karten
with open(input("In welcher Datei sind die Karten?\n"), "r", encoding="utf-8-sig") as file:
    data = file.read().split("\n")
longstock = data[0].split(" ")                      # vollständige Karte, aber mit unbekannten Anfang
knownmap = data[1].split(" ")                       # unvollständige Karte, aber mit korrektem Anfang
print("Bekannte Karte: " + " ".join(knownmap))
print("Longstocks Karte: " + " ".join(longstock))

while True:
    n = 0
    abort = False                                   # es wurde noch nicht erkannt, ob knownmap passt, oder nicht
                                                    # es wird kontrolliert, ob jedes Element aus longstock mit dem dazugehörigen aus knownmap passt
    while n < len(knownmap):                        # jedes Element wird durchgegangen
        if knownmap[n] != "?":                      # ist das zugehörige Element kein "?", wird kontrolliert ob beide Elemente gleich sind
            if longstock[n] != knownmap[n]:         # ist es ungleich,
                abort = True                        # können dadurch beide Karten nicht mehr passen
                break                               # die Kontrolle kann abgebrochen werden
        n = n + 1                                   # der Zähler wird um 1 erhöht, um das nächste Element auszuwählen
    if abort:                                       # wenn die Kontrolle negativ war, wird longstock um einen Eintrag rotiert
        lastelement = [longstock.pop()]             # das letze Element aus longstock wird entfernt,
        longstock = lastelement + longstock         # und an den Anfang gesetzt
    else:                                           # wenn die Kontrolle verlief, ohne einen Fehler zu finden, ist longstock richtig rotiert
                                                    # die richtige Karte, longstock wird ausgegeben
        print("Korrekte Karte: " + " ".join(longstock))
        break                                       # die Schleife wird unterbrochen, da ein Ergebnis gefunden wurde

input("Zum Beenden Enter drücken!\n")
