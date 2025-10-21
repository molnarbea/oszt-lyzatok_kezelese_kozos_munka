def elso_feladat(lista = []):
    print(lista)
    i = 0
    cv = 0
    osszesen=0
    while cv < len(lista):
        osszesen+=lista[i]
        cv+=1
        i+=1
    atlag=osszesen//len(lista)
    print(atlag)

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
