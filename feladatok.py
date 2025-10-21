def harmadik_feladat(lista=[]):
    cv=0
    i=0
    elegtelen=0
    while len(lista) > cv:
        if lista[i] == 1:
            elegtelen+=1
        i+=1
        cv+=1
    print(f"Összesen {elegtelen} diák kaputt elégtelent.")