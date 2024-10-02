from PIL import Image

def convert_image_to_grayscale():
    # Tentukan path gambar input dan output
    input_path = input("Masukkan jalur gambar (contoh: D:/Images/input.jpg): ")  # Masukkan path gambar Anda
    output_path = input("Masukkan jalur output untuk menyimpan gambar (contoh: D:/Images/output_cropped.jpg): ")  # Ganti dengan path output yang diinginkan
    # Buka gambar
    try:
        image = Image.open(input_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return
    
    # Ubah gambar ke grayscale
    grayscale_image = image.convert('L')

    # Simpan gambar grayscale
    grayscale_image.save(output_path)
    print(f"Gambar grayscale telah disimpan di: {output_path}")

    # Menunjukkan hasil gambar
    grayscale_image.show()
