#!/usr/bin/python

print("Junioraufgabe 1")

ladder = [[6, 27], [14, 19], [21, 53], [31, 42], [33, 38], [46, 62], [51, 59], [57, 96], [65, 85], [68, 80], [70, 76],
          [92, 98]]                                 # Leitern, jede enthält Start- und Endfeld
location = 0                                        # Variable für aktuellen Standpunkt
passed_locations = []                               # bereits betretene Felder
steps = 0                                           # Anzahl gemachter Züge
                                                    # Eingabe der Augenzahl
dice = int(input("Welche Augenzahl soll immer wieder hintereinander gewürfelt werden?\n"))

while True:                                         # jeder Durchlauf stellt einen Zug dar
    location = location + dice                      # Position wird um Augenzahl erhöht
    steps = steps + 1                               # Anzahl der gemachten Züge wird um eins erhöht
    if location > 100:                              # wenn der Spieler über Hundert ist,
        location = 200 - location                   # wird von Hundert Anzahl Schritte über Hundert abgezogen und als location gesetzt
    for i in ladder:                                # alle Leitern werden durchgegangen
        if location == i[0]:                        # wenn der Spieler am unteren Ende einer Leiter ist,
            location = i[1]                         # geht er an das obere Ende
            break
        if location == i[1]:                        # ist er am oberen,
            location = i[0]                         # geht er ans untere
            break
    if location == 100:                             # wenn der Spieler auf Feld 100 ankommt ist er im Ziel
        if steps == 1:                              # wenn nur ein Schritt nötig ist,
            print("1 Zug wird benötigt, um das Ziel zu erreichen!")  # muss der Singular verwendet werden
        else:                                       # sonst der Plural
            print(str(steps) + " Züge werden benötigt, um das Ziel zu erreichen!")
        break
    if location in passed_locations:                # ist der Spieler auf einem Feld, auf dem er schon war, ist er in einer Schleife
        print("Der Spieler ist auf Feld " + str(location) + " in einer Schleife!")
        break
    passed_locations.append(location)               # aktuelle Position wird vermerkt, falls Spieler wieder auf diesem Feld

input("Zum Beenden Enter drücken!\n")
