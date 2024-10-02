from PIL import Image

def rotate_image():
     # Meminta input path gambar dari pengguna
    input_path = input("Masukkan path gambar yang ingin diputar: ")  # Harus ke file gambar
    angle = float(input("Masukkan sudut rotasi (dalam derajat): "))  # Mengizinkan input desimal
    output_path = input("Masukkan path untuk menyimpan gambar yang diputar (beserta nama file dan ekstensi): ")
    try:
        # Membuka gambar
        image = Image.open(input_path)
        
        # Melakukan rotasi
        rotated_image = image.rotate(angle, expand=True)
        
        # Menyimpan gambar hasil rotasi
        rotated_image.save(output_path)
        print(f"Gambar berhasil disimpan di: {output_path}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


 

