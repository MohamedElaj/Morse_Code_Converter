from morse_art import logo

dictionary = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..',
    'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.',
    's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', 'ä':'.-.-',
    'ö':'---.', 'ß':'......', 'ü':'..--', 0:'-----', 1:'.----', 2:'..---', 3:'...--', 4:'....-', 5:'.....',
    6:'-....', 7:'--...', 8:'---..', 9:'----.', '.':'.-.-.-', ',':'--..--', '?':'..--..', '!':'-.-.--',
    '/':'-..-.', '(':'-.--.', ')':'-.--.-', '&':'.-...', ':':'---...', ';':'-.-.-.', '=':'-...-', '+':'.-.-.',
    '-':'-....-', '_':'..--.-', '"':'.-..-.', '$':'...-..-', '@':'.--.-.', ' ':'/'
           }


def in_morse_code():
    eingabe = input("Gib deinen Text ein! \n").lower()
    übersetzung = ''
    for i in eingabe:
        for j in dictionary:
            if i == j:
                übersetzung += f"{dictionary[j]} "

    print(übersetzung)


def in_text():
    eingabe = input("Gib deinen Text ein! \n").lower()
    eingabe_zeichen = eingabe.split()
    val_list = list(dictionary.values())
    key_list = list(dictionary.keys())
    übersetzung = ''

    for i in eingabe_zeichen:
        count = 0
        for j in val_list:
            count += 1

            if i == j:
                übersetzung += key_list[count - 1]

    print(übersetzung)


def main():
    print(logo)
    verfahren = True
    while verfahren:
        entscheidung = input("Willkommen im Morse-Code Übersetzer. Entscheiden Sie sich in den beiden unteren Zeilen zwischen zwei Verfahren.\n"
                             "Text in Morse-Code, dann tippe: 'm'\nMorse-Code in Text, dann tippe: 't'.\n").lower()

        if entscheidung == 'm':
            in_morse_code()

        elif entscheidung == 't':
            in_text()

        elif entscheidung != 't' or 'm':
            print("ungültige Angabe! Versuchen Sie es nochmal.\n")


main()