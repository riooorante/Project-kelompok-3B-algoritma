from PIL import Image     

def ukuran_gambar(Input_path,Output_path,left,top,right,bottom):
    try:
        image = Image.open(Input_path) # Membuka file gambar
        cropped_image = image.crop((left, top, right, bottom)) # Memotong gambar sesuai koordinat kiri atas dan kanan bawah sehingga terbentuk segii empat
        cropped_image.save(Output_path) # Menyimpan hasil di jalur output
        cropped_image.show() # Menunjukkan hasil gambar yang telah dipotong
        return f"Gambar berhasil dipotong dan disimpan di {Output_path}" # Akhir dari program
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

ukuran_gambar(
              "C:\\Users\jpael\OneDrive\Pictures\Ignition Teaser.png", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
              "C:\\Users\jpael\OneDrive\Pictures\Ignition Teaser14.png", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
              0,0,3000,1000
)
