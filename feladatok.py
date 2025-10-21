""" 
1. Mennyi a programozás jegyek átlaga? 

2. Összesen hány ötös van?  
"""


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