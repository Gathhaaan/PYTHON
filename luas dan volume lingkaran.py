#buat panggil library/modul fungsi math
import math

#mendefinisikan rumus 
def hitung_luas_lingkaran(jari_jari):
    luas = math.pi * jari_jari ** 2
    return luas

def hitung_keliling_lingkaran(jari_jari):
    keliling = 2 * math.pi * jari_jari 
    return keliling

#meminta input user
jari_jari = float(input("masukkan jari-jari lingkaran ="))

#menghitung luas lingkaran dan menampilkannya
luasLingkaran = hitung_luas_lingkaran(jari_jari)
print(f"hasil luas lingkaran dengan jari-jari {jari_jari} adalah {luasLingkaran}")

#menghitung keliling lingkaran
kelilingLingkaran = hitung_keliling_lingkaran(jari_jari)
print(f"hasil keliling lingkaran dengan jari-jari {jari_jari} adalah {kelilingLingkaran}")










