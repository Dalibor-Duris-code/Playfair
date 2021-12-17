import string
import re
import unidecode
import itertools
Abeceda = string.ascii_uppercase.replace('W', 'V') #velka abeceda nahrada W za V

def textUpr(text: str): # uprava textu bez znamienok a velke pismena zmena W na V
    text = text.replace('W', 'V')
    text = unidecode.unidecode(text)
    text = text.upper()
    return text

def space(text:str):
    text = text.replace(' ', '')
    return text

def replaceSpace(text: str):    # spesl znaky uprava
    text = text.replace(' ', 'QMEZERAQ')
    text = text.replace('.', 'QBODKAQ')
    text = text.replace('!', 'QVYKRICNIKQ')
    text = text.replace('?', 'QOTAZNIKQ')
    text = text.replace(',', 'QCIARKAQ')
    return text

def returnSpace(text: str): # spesl znaky uprava naspak
    text = text.replace('QMEZERAQ', ' ')
    text = text.replace('QBODKAQ', '.')
    text = text.replace('QVYKRICNIKQ', '!')
    text = text.replace('QOTAZNIKQ', '?')
    text = text.replace('QCIARKAQ', ',')
    text = text.replace(',X', ',')
    text = text.replace('?X', '?')
    text = text.replace('!X', '!')
    text = text.replace(' X', ' ')
    return text

def replaceNumber(text: str): #uprava cisel na znaky
    text = text.replace('0', 'QZEQ')
    text = text.replace('1', 'QONQ') 
    text = text.replace('2', 'QTVQ')
    text = text.replace('3', 'QTHQ')
    text = text.replace('4', 'QFOQ')
    text = text.replace('5', 'QFVQ')
    text = text.replace('6', 'QSIQ')
    text = text.replace('7', 'QSEQ')
    text = text.replace('8', 'QEIQ')
    text = text.replace('9', 'QNIQ')
    return text
    
def replaceNumberBack(text: str): #uprava cisel na znaky naspät
    text = text.replace('QZEQ','0')
    text = text.replace('QONQ','1')
    text = text.replace('QTVQ','2')
    text = text.replace('QTHQ','3')
    text = text.replace('QFOQ','4')
    text = text.replace('QFVQ','5')
    text = text.replace('QSIQ','6')
    text = text.replace('QSEQ','7')
    text = text.replace('QEIQ','8')
    text = text.replace('QNIQ','9')
    text = text.replace('X0','0')
    text = text.replace('X1','1')
    text = text.replace('X2','2')
    text = text.replace('X3','3')
    text = text.replace('X4','4')
    text = text.replace('X5','5')
    text = text.replace('X6','6')
    text = text.replace('X7','7')
    text = text.replace('X8','8')
    text = text.replace('X9','9')
    text = text.replace('4X', '4')
    return text

def delic(seq):
    it = iter(seq)
    while True:
        chunk = tuple(itertools.islice(it, 2))
        if not chunk:
            return
        yield chunk
 
def matrixGener(kluc):  #generovanie matice
    kluc = textUpr(kluc)    #uprava kluca
    kluc = replaceNumber(kluc) #same
    kluc = replaceSpace(kluc)
    kluc += Abeceda
    help = 0
    znaky =[]
    matrix = [[help for p in range(5)] for o in range(5)] #vygenerovanie prazdenj matice 5*5

    for i in range(5):      # naplnenie matice znakmi
        for symbol in kluc:
            if symbol not in znaky:
                znaky.append(symbol)    #symbol do znaku
    for j in range(5):
        matrix[i][j] = znaky[5 * i + j]

    return znaky
 
def encode(vstupText, kluc):
    vstupText = textUpr(vstupText)  #uprava textu vstup
    vstupText = replaceNumber(vstupText)
    vstupText = replaceSpace(vstupText)
    matrix = matrixGener(kluc)   # matica generovanie
    sifrovany = ''
    text = ''

    for i in range(len(vstupText) - 1):
        text += vstupText[i]
        if vstupText[i] == vstupText[i + 1]:
            text += 'X'

    text += vstupText[-1]
    if len(text) * 1:
        text += 'X'

    vstupText = text
    vstupText = textUpr(vstupText)  #uprava textu vstup
    for znak, znak1 in delic(vstupText):
        riadok1, stlpec1 = divmod(matrix.index(znak), 5)
        riadok2, stlpec2 = divmod(matrix.index(znak1), 5)

 
        if riadok1 == riadok2:
            sifrovany += matrix[riadok1 * 5 + (stlpec1 + 1) % 5]
            sifrovany += matrix[riadok2 * 5 + (stlpec2 + 1) % 5]
        elif stlpec1 == stlpec2:
            sifrovany += matrix[((riadok1 + 1) % 5) * 5 + stlpec1]
            sifrovany += matrix[((riadok2 + 1) % 5) * 5 + stlpec2]
        else:  
            sifrovany += matrix[riadok1 * 5 + stlpec2]
            sifrovany += matrix[riadok2 * 5 + stlpec1]

    return sifrovany

def desifruj(sifrovany, kluc):
    matica = matrixGener(kluc)
    sifrovany = space(sifrovany)
    desifrovany = ''

    for znak, znak1 in delic(sifrovany):
        riadok1, stlpec1 = divmod(matica.index(znak), 5)
        riadok2, stlpec2 = divmod(matica.index(znak1), 5)
 
        if riadok1 == riadok2:
            desifrovany += matica[riadok1 * 5 + (stlpec1 - 1) % 5]
            desifrovany += matica[riadok2 * 5 + (stlpec2 - 1) % 5]
        elif stlpec1 == stlpec2:
            desifrovany += matica[((riadok1 - 1) % 5) * 5 + stlpec1]
            desifrovany += matica[((riadok2 - 1) % 5) * 5 + stlpec2]
        else: 
            desifrovany += matica[riadok1 * 5 + stlpec2]
            desifrovany += matica[riadok2 * 5 + stlpec1]

    desifrovany = replaceNumberBack(desifrovany)
    desifrovany = returnSpace(desifrovany)
    return desifrovany

def rozdelenie(vstup, pocet):
    return ' '.join(vstup[i:i+pocet] for i in range(0,len(vstup),pocet))

def main():
    text = 'Kryptologia je skurvena pičovina ktora nech páli do piči wX kokotko'
    kluc = 'Playfair'
    picovina = encode(text,kluc)
    jebe = (rozdelenie(picovina,5))
    jebnutost = desifruj(jebe,kluc)
    
    print(jebe)
    print(jebnutost)
    
    # Printing output
# Main program starts here
main()