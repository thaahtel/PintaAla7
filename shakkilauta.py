# tee ratkaisu tänne

def pariton(sivu):
    rivi = ("10" * 10000)
    rivi = rivi[0:sivu - 1]
    print(rivi)

def parillinen(sivu):
    rivi = ("01" * 10000)
    rivi = rivi[0:sivu - 1]
    print(rivi)


def shakkilauta(sivu):
    i = 0

    kylki = int(sivu / 2)

    for i in range(0, kylki):
        print("10" * kylki)
        print("01" * kylki)


shakkilauta(4)

