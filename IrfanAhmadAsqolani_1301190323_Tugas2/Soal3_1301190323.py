"""
Total Kemunculan

Buatlah sebuah program Most Appear Item yang dapat mengurutkan barang berdasarkan jumlah kemunculannya. 
Jika ada barang yang duplicate kamu hanya perlu memunculkan sekali, namun kamu perlu menampilkan 
total kemunculan barang tersebut
Tulis fungsi untuk mengembalikan tiap item dengan jumlah item tersebut yang ada di dalam 
sebuah list yang diberikan sebagai parameternya.

Input: [“js”, “js”, “golang”, “ruby”, “ruby”, “js”, “js”]
Output: 
golang: 1 
ruby: 2 
js: 4
"""

def Total_Kemunculan(data):
    data.sort()
    output = []
    out_col = []
    kata = int(0)
    jumlah = int(0)
    for i in range(len(data)):
        if (i+1 != len(data)):
            if (data[i+1] == data[i]):
                jumlah +=1        
            else:        
                jumlah +=1
                out_col.append(data[i])
                out_col.append(jumlah)
                output.append(out_col)
                kata += 1
                jumlah = int(0)
                out_col = []
        else: 
            jumlah +=1
            out_col.append(data[i])
            out_col.append(jumlah)
            output.append(out_col)
            kata += 1
            jumlah = int(0)
            out_col = []
    output.sort(key=lambda x : x[1])
    return output

arr1 = ["js", "js", "golang", "ruby", "ruby", "js", "js"]
hasil1 = Total_Kemunculan(arr1)
for i in range(len(hasil1)):
    print(f"{hasil1[i][0]}: {hasil1[i][1]}")

print()
arr2 = ["danu", "danu", "alif", "indra", "indra", "kurniadi", "indra"]
hasil2 = Total_Kemunculan(arr2)
for i in range(len(hasil2)):
    print(f"{hasil2[i][0]}: {hasil2[i][1]}")