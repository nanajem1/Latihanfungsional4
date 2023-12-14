def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# example hof
kali_dua = perkalian(2)
result = kali_dua(11)
print(result)

# example currying
kali_dua = perkalian(2)
hasil = kali_dua(11)
print(hasil)
