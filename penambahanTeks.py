from PIL import Image, ImageDraw, ImageFont

def tambahkan_teks():
    foto = input("Masukkan gambar anda: ")
    hasil_foto = input("Masukkan nama output: ")
    foto = Image.open(foto)
    lebar, tinggi = foto.size
    print(f"ukuran gambar: {lebar}x{tinggi}")
    print("Masukkan koordinat penempatan teks: ")
    left = int(input("koordinat kiri (left): "))
    top = int(input("koordinat atas (top): "))
    posisi = (left, top)
    teks = input("Masukkan teks : ")
    print(
        """Font yang tersedia:
        arial.ttf
        ALGER.TTF
        calibri.ttf
        cambriab.ttf
        times.ttf"""
    )
    nama_font = input("Masukkan nama font: ")
    ukuran_font = int(input("Masukkan ukuran font: "))
    warna_font = input("Masukkan warna teks (nama warna atau hex): ")
    gambar = ImageDraw.Draw(foto)
    font = ImageFont.truetype(nama_font, ukuran_font)
    gambar.text(posisi, teks, fill=warna_font, font=font)
    foto.save(hasil_foto)
    foto.show(hasil_foto)

