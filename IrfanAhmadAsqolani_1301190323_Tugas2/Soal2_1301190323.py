"""
Penjumlahan Angka

Diberikan array angka yang diurutkan dan jumlah target,
temukan pasangan dalam array yang jumlahnya sama dengan target yang diberikan.
Tulis fungsi untuk mengembalikan indeks dari dua angka (yaitu pasangan) sedemikian rupa 
sehingga mereka menambahkan hingga target yang diberikan.

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
input: [2, 5, 9, 11], target=11
Output: [0, 2]
"""

def Penjumlahan(angka,target):
    index = []
    for i in range(len(angka)):
        for gerak in range(i+1,len(angka)):
            hitung = angka[i] + angka[gerak]
            if (hitung == target):
                index.append(i)
                index.append(gerak)
    return index

arr1 = [1,2,3,4,6]
hasil = Penjumlahan(arr1,6)
print(f"Penjumlahan yang tepat yaitu pada indeks ke- {hasil}")

arr2 = [2,5,9,11]
hasil2 = Penjumlahan(arr2,11)
print(f"Penjumlahan yang tepat yaitu pada indeks ke- {hasil2}")