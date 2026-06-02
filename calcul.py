import math
import random
import intro

liczbaKlastrów = 4
klastry = []
Centroidy = []

def test():
    print('\nLICZBA KLASTRÓW ', liczbaKlastrów)
    intro.wczytajDane()       
    intro.normalizujDane()     
    losujCentroidy()
    wypiszCentroidy()
    przypiszKrotkomNumeryKlastrów()
    utwórzKlastry()
    wypiszKlastry()
    newCentroidy()
    wypiszCentroidy()

def losujCentroide():
    # Generujemy 9 losowych ułamków (od 0.0 do 1.0) dla 9 cech liczbowych Doty
    centroida = []
    for _ in range(9):
        centroida.append(random.uniform(0.0, 1.0))
    return centroida

def losujCentroidy():
    Centroidy.clear()
    i = 1
    while i <= liczbaKlastrów:
        Centroidy.append(losujCentroide())
        i = i + 1

def wypiszCentroide(centroida):
    # Wypisanie współrzędnych centroidu (9 liczb)
    print(" ".join(['%6.3f' % cecha for cecha in centroida]))

def wypiszCentroidy():
    print('CENTROIDY')
    for centroida in Centroidy:
        wypiszCentroide(centroida)

def EuklidesPower(krotkaNormal, centroida):
    # Liczymy odległość TYLKO dla kolumn liczbowych (od indeksu 2 do 10)
    # Indeks 0 (nazwa) i 1 (typ atrybutu) ignorujemy
    suma = 0
    for i in range(2, 11):
        dif = centroida[i - 2] - krotkaNormal[i]
        suma += math.pow(dif, 2)
    return suma

def przypiszKrotkomNumeryKlastrów():
    for krotkaNormal in intro.krotkiNormal:
        minimum = 1e100
        minimumIndex = 0
        for i in range(len(Centroidy)):
            next_dist = EuklidesPower(krotkaNormal, Centroidy[i])
            if next_dist < minimum:
                minimum = next_dist
                minimumIndex = i
        # Zapisujemy znaleziony numer klastra na końcu (indeks 11)
        krotkaNormal[11] = minimumIndex

def utwórzKlastry():
    klastry.clear()
    for i in range(0, len(Centroidy)):
        klaster = []
        for krotka in intro.krotkiNormal:
            if krotka[11] == i:
                klaster.append(krotka)
        klastry.append(klaster)

def wypiszKlaster(nrKlastra):
    print('\nNUMER KLASTRA ', nrKlastra, ' (Liczba bohaterów:', len(klastry[nrKlastra]), ')')
    for krotka in klastry[nrKlastra]:
        # Wypisujemy nazwę [0], atrybut [1] i numer klastra [11]
        print('%-25s %-5s Klastr: %d' % (krotka[0], krotka[1], krotka[11]))

def wypiszKlastry():
    for numer in range(0, len(Centroidy)):
        wypiszKlaster(numer)

def newCentroide(klaster):
    if len(klaster) == 0:
        return losujCentroide()
    
    # Tworzymy tablicę 9 zer do sumowania każdej cechy
    sumy = [0.0] * 9
    for krotka in klaster:
        for i in range(2, 11):
            sumy[i - 2] += krotka[i]
            
    # Dzielimy sumę przez liczbę bohaterów w klastrze (znajdujemy nową średnią)
    nowa_centroida = []
    for s in sumy:
        nowa_centroida.append(s / len(klaster))
    return nowa_centroida

def newCentroidy():
    Centroidy.clear()
    print('\nprzesunięto centroidy ------------')
    for nr in range(liczbaKlastrów):
        Centroidy.append(newCentroide(klastry[nr]))
