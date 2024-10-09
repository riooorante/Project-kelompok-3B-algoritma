from PIL import Image, ImageEnhance
import os

def adjust_brightness(image_path,output_path,level):
    """Mengubah kecerahan gambar berdasarkan level yang ditentukan."""
    # Faktor kecerahan berdasarkan level yang ditentukan
    brightness_factors = {
        'sangat gelap': 0.2,
        'gelap': 0.5,
        'normal': 1.0,
        'cerah': 1.5,
        'sangat cerah': 2.0
    }
    
    # Mendapatkan faktor kecerahan dari level yang diberikan
    factor = brightness_factors.get(level.lower(), 1.0)  # Default ke 'normal' jika level tidak valid

    # Cek apakah file gambar ada
    if not os.path.isfile(image_path):
        print(f"File gambar tidak ditemukan: {image_path}")
        return

    image = Image.open(image_path) # Membuka file gambar
    enhancer = ImageEnhance.Brightness(image) # Menggunakan fungsi pencerahan dari pillow
    brightened_image = enhancer.enhance(factor) #  Menentukan skala kecerahan gambar
    brightened_image.save(output_path) # Menyimpan hasil di jalur output
    brightened_image.show(output_path) # Menunjukkan hasil pencerahan gambar

