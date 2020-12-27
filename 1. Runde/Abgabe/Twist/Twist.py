# !/usr/bin/python

# Folgende Annahmen wurden genommen:
# -In dem Hauptverzeichnis liegt mindestens eine Datei, utf-8 encodiert, in der ein Text ist
# -Es wird nicht erwartet, dass der Text perfekt wieder enttwistet wird

print("Twist")


from random import shuffle
                                                    # Liste häufiger Satzzeichen
punctuation_marks = [",",
                     ";",
                     ".",
                     ":",
                     "–",
                     "_",
                     "#",
                     "'",
                     "+",
                     "*",
                     "/",
                     "?",
                     ")",
                     "(",
                     "&",
                     "%",
                     "!",
                     "@",
                     "<",
                     ">",
                     "|",
                     '"',
                     '„',
                     '“',
                     "\n",
                     "1",
                     "2",
                     "3",
                     "4",
                     "5",
                     "6",
                     "7",
                     "8",
                     "9",
                     "0",
                     "-"]
                                                    # Dictionary mit häufigen deutschen Wörtern
words = {"a": [],
         "b": [],
         "c": [],
         "d": [],
         "e": [],
         "f": [],
         "g": [],
         "h": [],
         "i": [],
         "j": [],
         "k": [],
         "l": [],
         "m": [],
         "n": [],
         "o": [],
         "p": [],
         "q": [],
         "r": [],
         "s": [],
         "t": [],
         "u": [],
         "v": [],
         "w": [],
         "x": [],
         "y": [],
         "z": [],
         "ä": [],
         "ö": [],
         "ü": []}
                                                    # Dictionary wird aufgefüllt
with open("woerterliste.txt", "r", encoding="utf-8-sig") as file:
    for line in file:
        for i in words:
            if line.lower()[0] == i:
                words[i].append(line.lower().replace("\n", ""))

text = []                                           # eingegebener Text
                                                    # Text wird eingelesen
with open(input("In welcher Datei ist der Text?\n"), "r", encoding="utf-8-sig") as file:
    for line in file:
        if line != "\n":
            text.append(line.replace("\n", "").split(" "))


                                                    # Funktion zum Twisten eines wortes mit Satzzeichen vorn und hinten
def twist(word):
    if len(word) <= 3:                              # wenn das word weniger als drei Buchstaben hat, kann nichts geändert werden
        return word
    word = list(word)
    begin = []                                      # Liste aller Satzzeichen vor dem word und dem ersten Buchstaben
    end = []                                        # Liste aller Satzzeichen nach dem word und dem letzten Buchstaben
                                                    # alle Satzzeichen vor dem word werden entfernt
    while word[0] in punctuation_marks:
        begin.append(word[0])
        del word[0]
                                                    # der erste Buchstabe wird entfernt
    begin.append(word[0])
    del word[0]
                                                    # alle Satzzeichen nach dem word werden entfernt
    while word[-1] in punctuation_marks:
        end.append(word[-1])
        del word[-1]
                                                    # der letzte Buchstabe wird entfernt
    end.append(word[-1])
    del word[-1]
                                                    # end wird umgedreht, weil es von hinten nach vorne befüllt wurde
    end = reversed(end)
    shuffle(word)
                                                    # das wort wird wieder zusammengesetzt und zurückgegeben
    return "".join(begin) + "".join(word) + "".join(end)


                                                    # Funktion zum Enttwisten eines Wortes
def untwist(word):
    word = list("".join(word).lower())              # Groß- und Kleinschreibung wird nicht berücksichtigt
                                                    # es werden alle Wörter in der dictionary durchgegangen, die mit dem richtigen Buchstaben anfangen
    for testword in words[word[0]]:
        compword = list(testword)                   # das aktuelle Wort wird in eine Liste konvertiert
                                                    # nur Wörter mit der richtigen Länge und Endbuchstaben kommen in die engere Auswahl
        if len(list(testword)) == len(word) and list(testword)[-1] == word[-1]:
            right = True                            # noch kann das Wort passen
            n = 0
                                                    # jeder Buchstabe wird überprüft
            while n < len(word):
                if word[n] in compword:             # ist der aktuelle Buchstabe vorhanden,
                    compword.remove(word[n])        # wird er entfernt
                else:                               # wenn nicht,
                    right = False                   # ist das Wort falsch, es wird das nächste getestet
                    break
                n = n + 1
            if right:                               # wurde ein Wort gefunden,
                return list(testword)               # wird es zurückgegeben
    return word                                     # wurde keins gefunden, wird das getwistete Wort zurückgegeben


                                                    # Text wird getwistet
twistedtext = []                                    # gtwisteter Text
for line in text:                                   # Zeile für Zeile
    twistedline = []                                # getwistete Zeile
    for word in line:                               # Wort für Wort
        twistedline.append(twist(word))             # Wort wird zur Zeile hinzugefügt
    twistedtext.append(twistedline)                 # Zeile wird zum Text hinzugefügt

                                                    # getwisteter Text wird ausgegeben
for line in twistedtext:
    print(" ".join(line))
print("\n\n\n")
print("-----------------------------------------------------------------------------------------------------------")
print("\n\n\n")

                                                    # Text wird enttwistet
untwistedtext = []                                  # enttwisteter Text
for line in twistedtext:                            # Zeile für Zeile
    untwistedline = []                              # enttwistete Zeile
    for word in line:
        if len(word) <= 3:                          # wenn das Wort weniger als vier Buchstaben hat, wurde nichts geändert
            untwistedline.append(word)              # es wird so, wie es ist übernommen
            continue                                # das nächste Wort wird enttwistet
                                                    # genau, wie beim Twisten werden alle Satzzeichen entfernt, ignoriert und später wieder hinzugefügt
        word = list(word)
        begin = []
        end = []
        while word[0] in punctuation_marks:
            begin.append(word[0])
            del word[0]
        while word[-1] in punctuation_marks:
            end.append(word[-1])
            del word[-1]
        end = reversed(end)
                                                    # ist das Wort großgeschrieben wird dies vermerkt
        if word[0].isupper():
            firstchar = word[0]
        else:
            firstchar = ""
                                                    # das Wort wird wieder zusammengesezt
                                                    # das Wort bekommt seine Satzzeichen am Ende zurück
        word = list("".join(untwist(word)) + "".join(end))
        if firstchar != "":                         # wenn Das Wort großgeschrieben ist,
            del word[0]                             # wird der erste Buchstabe entfernt
                                                    # das Wort bekommt seine Satzzeichen am Anfang und ersten Buchstaben wieder und wird der Zeile hinzugefügt
        untwistedline.append("".join(begin) + firstchar + "".join(word))
    print(" ".join(untwistedline))
    untwistedtext.append(untwistedline)             # die Zeile wird dem Text hinzugefügt

print("\n\n\n\n\n")
print("-----------------------------------------------------------------------------------------------------------")
input("Zum Beenden Enter drücken!")
