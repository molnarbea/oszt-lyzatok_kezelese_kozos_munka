import random

def elso_feladat(lista = []):
    i = 0
    cv = 0
    osszesen=0
    while cv < len(lista):
        osszesen+=lista[i]
        cv+=1
        i+=1
    atlag=osszesen//len(lista)
    print(atlag)
    return atlag

def masodik_feladat(lista = []):
    cv = 0
    otos = 0
    i = 0
    while cv < len(lista):
        if lista[i] == 5:
            otos+=1
        i+=1   
        cv+=1
    return otos

def harmadik_feladat(lista=[]):
    cv=0
    i=0
    elegtelen=0
    while len(lista) > cv:
        if lista[i] == 1:
            elegtelen+=1
        i+=1
        cv+=1
    return elegtelen

def negyedik_feladat(lista=[]):
    cv=0
    i=0
    diak=0
    while len(lista) > cv:
        if lista[i] == 1:
            diak=i+1
        i+=1
        cv+=1
    return diak



def hetedik_feladat():
    jegy_lista = []
    cv= 0 
    while cv < 17:
        veljegy = random.randint(1,6)
        if veljegy == 6:
            jegy = 5
        else:
            jegy = veljegy
        jegy_lista.append(jegy)
        cv+=1
    return jegy_lista
def otodik_feladat(lista=[],jegy=0):
    szam=0
    cv=0
    i=0
    while len(lista) > cv:
        if lista[i] == jegy:
            szam+=1
        i+=1
        cv+=1
    return szam
    
