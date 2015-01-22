#!/usr/bin/python

#Das Modul 'sys' wird importiert um Zugriff auf die via Kommandozeile übergebenen Parameter zu erhalten.
import sys

#Das Array Alphabet enthält alle Buchstaben, die wir verschlüsseln können wollen.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#sys.argv[1] und sys.argv[2] sind die Parameter, die über die Kommandozeile übergeben werden.
plaintext = sys.argv[1] 
offset = int(sys.argv[2])
#Die Länge des unverschlüsselten Textes wird ermittelt.
length = len(plaintext)
#Die aktuelle Position im Text wird initialisiert.
position = 0
#In den hier noch leer initialisierten String `chiffre` wird nach und nach das Chiffrat geschrieben.
chiffre = ''

#Solange die Variable 'position' kleiner der Variable 'length' ist, wird folgendes ausgeführt...
while position < length:
        #Der Variablen 'letter, wird der Buchstabe an der Stelle 'position' im Plaintext zugewiesen.
	letter = plaintext[position]
        #Falls der Buchstabe kein Alphanumerisches Zeichen ist (also kein Buchstabe, sondern z. B. ein Leerzeichen oder ein Satzzeichen).
	if not letter.isalpha():
                #Hänge das Zeichen an das Ende des Strings 'chiffre' an.
		chiffre = chiffre + letter
        #Sonsts (Wenn der Buchstabe ein Alphanumerisches Zeichen ist):
	else:

		currentletter = alphabet.index(letter.lower())
		newletter = (currentletter + offset) % 26
		newl = alphabet[newletter]
		if letter.isupper():
			newl = newl.upper()
		chiffre = chiffre + newl 
	position = position + 1

print chiffre
