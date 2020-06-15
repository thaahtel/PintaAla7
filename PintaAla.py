def Ohjeet():
    print('''
Pinta-alan laskemista. Valitse seuraavista

(1) Kolmio
(2) Neliö
(3) Suorakulmio
(4) Ympyrä

(Q) Lopeta  
    ''')

def Kolmio():
    k = float(input('Anna kolmion kannan leveys: '))
    h = float(input('Anna kolmion korkeus: '))
    Ala = k * h * 0.5
    print('Kolmion ala on: ' + str(Ala))

def Nelio():
    x = float(input('Anna neliön sivun pituus: '))
    Ala = x * x
    print('Neliön ala on: ' + str(Ala))

def Suorakulmio():
    k = float(input('Anna suorakulmion sivun pituus: '))
    h = float(input('Anna suorakulmion korkeus: '))
    Ala = k * h
    print('Suorakulmion ala on: ' + str(Ala))

def Ympyra():
    x = float(input('Anna ympyrän säde: '))
    Ala = round(x * x * 3.1415, 8)
    print('Ympyrän ala on: ' + str(Ala))

syote = ""
Ohjeet()

while True:
    syote = input('valintasi: ')

    if syote == '1':
        Kolmio()
        Ohjeet()

    elif syote == '2':
        Nelio()
        Ohjeet()

    elif syote == '3':
        Suorakulmio()
        Ohjeet()

    elif syote == '4':
        Ympyra()
        Ohjeet()

    elif syote.capitalize() == 'Q':
        print('Lopetetaan')
        break

    else:
        print('En ymmärrä, yritä uudestaan')

