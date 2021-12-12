# Nama: Irfan Ahmad Asqolani
# NIM: 1301190323
# Divisi: Software Engineer

Baris = int(input("Masukan Panjang Baris Segitiga: "))

# Soal 1 half Pyramid pattern
print("\nhalf Pyramid pattern")
for i in range(1,Baris+1):
    for j in range(0,i):
        print("*", end=" ")
    print()
print()

# Soal 2 half Inverted pyramid pattern
print("half Inverted pyramid pattern")
for i in range(Baris,0,-1):
    for j in range(0,i):
        print("*", end=" ")
    print()
print()

# Soal 3 half pyramid pattern mirrored
print("half pyramid pattern mirrored")
space = 2*Baris-2
for i in range(0,Baris):
    for j in range(0,space):
       print(end=" ")
    space -= 2

    for j in range(0, i+1):
        print("*", end=" ")
    print()    
print()

# Soal 4 full pyramid pattern
print("full pyramid pattern")
space = Baris-1
for i in range(0,Baris):
    for j in range(0,space):
       print(end=" ")
    space -= 1

    for j in range(0, i+1):
        print("*", end=" ")
    print()    
print()

# Soal 5 full pyramid pattern mirrored
print("full pyramid pattern mirrored")
space = 0
for i in range(Baris,0,-1):
    for j in range(0,space):
        print(end=" ")
    space += 1
    for j in range(0,i):
        print("*", end=" ")
    print()
print()

print("Nama : Irfan Ahmad Asqolani")
print("NIM : 1301190323")
print("Divisi : Software Engineer")
