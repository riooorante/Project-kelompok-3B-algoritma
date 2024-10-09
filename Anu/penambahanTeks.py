from PIL import Image, ImageDraw, ImageFont

def tambahkan_teks(input_path,output_path,teks,left,top,nama_font,font_size,warna_font):
    # Membuka file gambar
    input_path = Image.open(input_path)
    # Menentukan posisi teks
    posisi = (left, top)
    # Mengolah gambar
    gambar = ImageDraw.Draw(input_path)
    # Mengolah nama font dan ukuran teks
    font = ImageFont.truetype(nama_font, font_size)
    # Menempatkan posisi dan warna teks
    gambar.text(posisi, teks, fill=warna_font, font=font)
    input_path.save(output_path) # Menyimpan hasil di output
    input_path.show(output_path) # Menunjukkan hasil gambar yang telah ditambahkan teks

