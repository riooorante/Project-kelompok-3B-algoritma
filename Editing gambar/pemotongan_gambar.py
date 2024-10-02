from PIL import Image     

def ukuran_gambar():
    Gambar = input("Masukkan jalur gambar (contoh: D:/Images/input.jpg): ")
    Hasil = input("Masukkan jalur output untuk menyimpan gambar (contoh: D:/Images/output_cropped.jpg): ")
    gambar = Image.open(Gambar)
    lebar, tinggi = gambar.size
    print(f"Ukuran gambar: {lebar}x{tinggi}")
    print("Masukkan koordinat pemotongan gambar:")
    left = int(input("Koordinat kiri (left): "))
    top = int(input("Koordinat atas (top): "))
    right = int(input("Koordinat kanan (right): "))
    bottom = int(input("Koordinat bawah (bottom): "))
    try:
        image = Image.open(Gambar)
        cropped_image = image.crop((left, top, right, bottom))
        cropped_image.save(Hasil)
        print(f"Gambar berhasil dipotong dan disimpan di {Hasil}")
        cropped_image.show()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
