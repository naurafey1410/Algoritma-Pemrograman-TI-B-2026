# function dan validasi data 

def rata_rata(nilai):
    if len(nilai) == 0:
        return "Data kosong"
    
    total = 0
    for n in nilai:
        total += n

    return total / len(nilai)

hasil = rata_rata([80, 75, 90, 60, 85])
print(hasil)