import feladatok

lista=[5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3]

elegtelen=feladatok.harmadik_feladat(lista)
diak=feladatok.negyedik_feladat(lista)

otosok = feladatok.masodik_feladat(lista)
print(f"Összesen {otosok} van")

feladatok.harmadik_feladat(lista)

dupla = feladatok.hetedik_feladat()
print(dupla)


elegtelen=feladatok.harmadik_feladat(lista)
diak=feladatok.negyedik_feladat(lista)

print(f"Összesen {elegtelen} diák írt elégtelent.")
print(f"A {diak}. diák írt elégtelent.")

egy=feladatok.otodik_feladat(lista,1)
ketto=feladatok.otodik_feladat(lista,2)
harom=feladatok.otodik_feladat(lista,3)
negy=feladatok.otodik_feladat(lista,4)
ot=feladatok.otodik_feladat(lista,5)
print(f"1. {"*"*egy}\n2. {"*"*ketto}\n3. {"*"*harom}\n4. {"*"*negy}\n5. {"*"*ot}")