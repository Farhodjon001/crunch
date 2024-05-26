import itertools as t
chars = input("Belgilarni kiriting : ")
min = int(input("Minimum takrorlanishlar soni : "))
max = int(input("Maksimum takrorlanishlar soni : "))
output = input("Output File : ")

if output == "" or output is None:
    file = open(chars+".txt", 'w')
else:
    file = open(output, 'w')
if min == max:
    for a in t.product(chars, repeat= min):
        s = "".join(a)
        file.write(s+"\n")

elif min < max:
    for i in range(min, max+1):
        for a in t.product(chars, repeat= i):
            s = "".join(a)
            file.write(s+"\n")


else:
    print("Maxsimum minimumdan katta bo'lishi kerak ")
    exit()
if output == "" or output is None:
    print("File shu nom bilan saqlandi : "+chars+".txt")
else:
    print("File shu nom bilan saqlandi : "+output)

