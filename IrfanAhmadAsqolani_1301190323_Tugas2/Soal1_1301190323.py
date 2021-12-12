"""
Angka Muncul Sekali 

Buat program sesuai dengan deskripsi di bawah. Input merupakan variable string berisi kumpulan angka.
Output merupakan list / array berisi angka yang hanya muncul 1 kali pada input.
Tulis fungsi untuk mengembalikan sebuah array berisi angka angka yang hanya muncul sekali 
dalam sebuah string yang ada pada parameter fungsi tersebut.

Input: “76523752”
Output: [6, 3] 
Input: “1122”
Output: []
"""

def Muncul_Sekali(angka):
    data = list(map(int, angka))    
    data.sort()
    output = []
    kata = int(0)
    jumlah = int(0)
    for i in range(len(data)):
        if (i+1 != len(data)):
            if (data[i+1] == data[i]):
                jumlah +=1        
            else:        
                jumlah +=1
                if (jumlah == 1):
                    output.append(data[i])
                kata += 1
                jumlah = int(0)
        else: 
            jumlah +=1
            if (jumlah == 1):
                output.append(data[i])
            kata += 1
            jumlah = int(0)    
    return output

inputan1 = "76523752"
hasil1 = Muncul_Sekali(inputan1)
print("Angka yang hanya muncul sekali",hasil1)

inputan2 = "1122"
hasil2 = Muncul_Sekali(inputan2)
print("Angka yang hanya muncul sekali",hasil2)

inputan3 = "1234123"
hasil3 = Muncul_Sekali(inputan3)
print("Angka yang hanya muncul sekali",hasil3)
