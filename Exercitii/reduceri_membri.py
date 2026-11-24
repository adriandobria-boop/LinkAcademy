membru = input("sunteti membru?, DA / NU \n").upper()
suma_achizitiei = float(input("introduceti suma achizitiei: \n"))


if suma_achizitiei < 100:
    if membru == ("DA"):
        print("ai reducere de 5%")
    else:
        print("nu ai reducere")
        
elif suma_achizitiei <= 500:
    if membru == ("DA"):
        print("ai reducere de 10%")
    else:
         print("ai reducere de 5%")
         

elif suma_achizitiei < 1000:
    if membru == ("DA"):
        print("ai reducere de 15%")
    else:
        print("ai reducere de 10%")
        
else:
    if membru == ("DA"):
        print("ai reducere de 20%")
    else:
        print("ai reducere de 15%")
    



   