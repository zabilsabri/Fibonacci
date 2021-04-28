n = int(input("MASUKKAN ANGKA: "))

d1 = 0
d2 = 1
jawaban = [0]

for i in range(n - 1):
    hasil = d2 + d1
    d1 = d2
    d2 = hasil
    jawaban.append(d1)

print(jawaban)