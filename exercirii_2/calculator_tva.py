lei=float(input("suma_fara_tva:"))
tva = 0.21 * float(lei)
suma_totala=lei+tva

print("suma_totala", round(suma_totala, 2), "lei")
print("tva", round(tva, 2), "lei")