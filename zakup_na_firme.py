def odliczenie_na_firme(amount):
    vat = (amount - (amount * 0.23))
    odliczenie = (vat * 0.19)
    return odliczenie



amount = float(input("BRUTTO: "))
result = odliczenie_na_firme(amount)
print("Do odliczenia: ", (round(result, 2)))


