print("\n---------1---------\n")
print("\n---------2---------\n")

# print(test._set)

print("\n---------3---------\n")

level43=[12,1,5,10,14,1,2]

for x in level43:
    print("*"*x)

print("\n---------4-1---------\n")

while True:
    ZipCode=str(input("Enter a zip code: "))
    
    if ZipCode.isdigit() and len(ZipCode) == 5 and ZipCode[0] != "0":
        break
    else:
        print("ERROR! ENTER VALID CODE")

if ZipCode[0] == '1':
    status = "Tallinn"
elif ZipCode[0] == '2':
    status = "Narva, Narva-Jõesuu"
elif ZipCode[0] == '3':
    status = "Kohtla-Järve"
elif ZipCode[0] == '4':
    status = "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa"
elif ZipCode[0] == '5':
    status = "Tartu linn"
elif ZipCode[0] == '6':
    status = "Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
elif ZipCode[0] == '7':
    status = "Viljandimaa, Järvamaa, Harjumaa, Raplamaa"
elif ZipCode[0] == '8':
    status = "Pärnumaa"
elif ZipCode[0] == '9':
    status = "Läänemaa, Hiiumaa, Saaremaa"
else:
    status = "ERROR!"
    
print(f"\nZIPCODE = {status}")
if int(ZipCode[0]) <= 3 and int(ZipCode[0]) != 0:
    print("Оставайтесь дома!")
else:
    print("Носите маски!")


print("\n---------4-2---------\n")
word42=str(input("Enter a Word: "))
list_word42=list(word42)
list_word42.insert(0,list_word42[-1])
list_word42.insert(-1,list_word42[1])
list_word42.pop(1)
list_word42.pop(-1)
print(list_word42)

print("\n---------4-3---------\n")




print("\n---------4-4---------\n")

data44 = [1,6,2,7,3,-1,43,2,-32,235,23]


print(data44)
for x in range(len(data44)):
    data44[x] = abs(int(data44[x]))

data44.sort(reverse=True)
print( data44 )

print("\n---------5---------\n")
print("\n---------6---------\n")


print("\n---------6-2---------\n")

järjendi0 = ['a','b','c','d','e','f']
järjendi1 = []

for x in range(len(järjendi0)-1):
    järjendi1.append(järjendi0[x]*(x+1))

print(järjendi1)

print("\n---------6-6---------\n")

EestiKeel = ['üks', 'kaks', 'kolm', 'neli']
IngliseKeel = ['one', 'two', 'three', 'four']
ItaaliaKeel = ['uno', 'due', 'tre', 'quattro']

for x in range(4):
    print(f" {x+1} {EestiKeel[x]} - {IngliseKeel[x]} - {ItaaliaKeel[x]}")

print("\n---------7---------\n")
print("\n---------8---------\n")
print("\n---------9---------\n")
print("\n--------10---------\n")
