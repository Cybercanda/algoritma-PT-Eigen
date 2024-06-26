def terpanjang(kalimat):
    kata = kalimat.split()
    kata_terpanjang = max(kata, key=len)

    return kata_terpanjang
     
kalimat = "Saya sangat senang mengerjakan soal algoritma"

print(terpanjang(kalimat))