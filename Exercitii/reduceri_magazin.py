suma_achizitiei = float(input("introduceti suma achizitiei: \n"))

if suma_achizitiei < 100:
    print("nu ai reducere")
elif suma_achizitiei <= 500:
    print("ai reducere de 5%") 
elif suma_achizitiei < 1000:
    print("ai reducere de 10%")
else:
    print("ai reducere de 15%")
