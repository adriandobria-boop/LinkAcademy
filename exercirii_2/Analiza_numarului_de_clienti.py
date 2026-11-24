luni = int(input("introduceti numarul de clienti pentru Luni:")) 
marti = int(input("introduceti numarul de clienti pentru Marti:")) 
miercuri = int(input("introduceti numarul de clienti pentru Miercuri:")) 
joi = int(input("introduceti numarul de clienti pentru Joi:"))
vineri = int(input("introduceti numarul de clienti pentru Vineri:"))
sambata = int(input("introduceti numarul de clienti pentru Sambata:"))
duminica = int(input("introduceti numarul de clienti pentru Duminica:"))

clienti_saptamana = luni + marti + miercuri + joi + vineri + sambata + duminica

clienti_zile_lucratoare = luni + marti + miercuri + joi + vineri 

clienti_weekend = sambata + duminica

duminica_mai_mare = duminica > sambata

zile_lucratoare_mai_mare = clienti_zile_lucratoare > clienti_weekend

saptamana_de_suuces = clienti_saptamana > 1000 or clienti_weekend > 500

print("\nRAPORT SAPTAMANAL" )
print(f"Total clienti pe saptamana, {clienti_saptamana}")
print(f"Total clienti in zilele lucratoare, {clienti_zile_lucratoare}")
print(f"Total clienti in weekend, {clienti_weekend}")
print(f"Duminica au fost mai multi clienti decat sambata, {duminica_mai_mare} ")
print(f"Au fost mai multi clienti in zilele lucratoare decat in weekend, {zile_lucratoare_mai_mare}")
print(f"A fost o saptamana de succes, {saptamana_de_suuces}")

    

    