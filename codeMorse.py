"""
Modules nécessaires :
playsound - time.

Mandatory modules :
playsound - time.

>>> python -m pip install playsound --update

- Partie du Projet Expirémental et Numérique.

@ZakousseMC
"""

from playsound import playsound
from time import sleep

class morse:
    def TextToMorse(originalText: str):
        """
        Converti du texte en morse.
        Convert text to morse code.

        >>> TextToMorse("sos")
        ...---...
        """
        alphabet = {"A":".- ", "Â":".- ", "À": ".- ", "B":"-... ", "C":"-.-. ", "D":"-.. ","Ê":". ", "É": ". ", "È":". ", "E":". ", 
                    "F":"..-. ", "G":"--. ", "H":".... ", "I":".. ", "J":".--- ", "K":"-.- ", 
                    "L":".-.. ", "M":"-- ", "N":"-. ", "O":"--- ", "P":".--. ", "Q":"--.- ", 
                    "R":".-. ", "S":"... ", "T":"- ", "U":"..- ", "V":"...- ", "W":".-- ", 
                    "X":"-..- ", "Y":"-.-- ", "Z":"--.. ", "1":".---- ", "2":"..--- ", "3":"...-- ", 
                    "4":"....- ", "5":"..... ", "6":"-.... ", "7":"--... ", "8":"---.. ", "9":"----. ", 
                    "0":"----- ", ", ":"--..-- ", ".":".-.-.- "," ":"/ ", "?":"..--.. ", "/":"-..-. ", "-":"-....- ", 
                    "(":"-.--.", ")":"-.--.- "}

        converted = ""


        for letter in originalText:
            letter = letter.upper()
            converted += alphabet[letter]

        return converted

    def MorseToSound(morseText: str):
        """
        Converti du morse textuel en morse sonore.
        Convert textual morse code to sound.

        >>> MorseToSound("...---...")
        audio
        """
        for char in morseText:
            if char == ".":
                playsound("dot.wav")
            if char == "-":
                playsound("dash.wav")
            if char == "/":
                sleep(0.5)
            else:
                pass

        return "Done !"

print("-!- Attention -!- Le texte écrit ne doit pas comporter de symboles (apostrophes) ni de ponctuation !")
subjectText = str(input("Entrez le texte que vous souhaitez traduire en morse : "))
convertedText = morse.TextToMorse(subjectText)
#print(convertedText)
convertedSound = morse.MorseToSound(convertedText)