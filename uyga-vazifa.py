menyu = {}

while True:
    ovqat_nomi = input("Ovqat nomini kiriting: ")
    ovqat_narxi = int(input(f"{ovqat_nomi.title()} narxini kiriting: "))
    menyu[ovqat_nomi] = ovqat_narxi
    savol = input("Davom etasizmi? ha/yoq: ")
    if savol == 'yoq':
        break
print(menyu)
    
buyurtma = []

while True:
    ovqat_nomi = input("Ovqat nomini kiriting: ")
    buyurtma.append(ovqat_nomi)
    savol = input("Davom etasizmi: ha/yoq")
    if savol == 'yoq':
        break
print(buyurtma)

for i in buyurtma:
    if i in menyu:
        print(f"{i}ning narxi {menyu[i]} ga teng")
    else:
        print("Bu ovqat bizda yoq")