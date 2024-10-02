# Brightness feature

Brightness feature adalah paket Python yang digunakan untuk menyesuaikan kecerahan gambar. Paket ini memudahkan pengguna dalam mengubah kecerahan gambar sesuai kebutuhan.

## Fitur

- Menyesuaikan kecerahan gambar
- Mendukung berbagai format gambar

## Instalasi

Untuk menginstal Brightness feature, jalankan perintah berikut:
```bash
pip install .


# Cara penggunaan di google colab
!pip install git+your URL

# Instal pillow jika belum menginstalnya 
pip install Pillow

# Masukkan gambar
from google.colab import files
uploaded = files.upload()

#cara menyimpan gambar di : output
image_path = 'nama file.jpg'
output_path = 'nama file yang ingin di simpan.jpg'
level = 'sangat gelap', 'gelap', 'normal', 'cerah', 'sangat cerah' #pilih salah satu
Brightness_feature.adjust_brightness(image_path, output_path, level)
files.download(output_path)

'Deskripsi'
# Memuat gambar
image_path = 'nama file.jpg'
output_path = 'nama file yang ingin di simpan.jpg'


# Menyesuaikan kecerahan
level = 'sangat gelap', 'gelap', 'normal', 'cerah', 'sangat cerah'

# Menyimpan gambar hasil
Brightness_feature.adjust_brightness(image_path, output_path, level)

# Simpan di perangkat
files.download(output_path)


# Jika belum jelas!
help(Brightness_feature.adjust_brightness)

# Keterangan
Help on function adjust_brightness in module motipy.adjuster:

adjust_brightness(image_path, output_path, level)
    Mengubah kecerahan gambar berdasarkan level yang ditentukan.
    
    Args:
        image_path (str): Path ke file gambar input.
        output_path (str): Path untuk menyimpan gambar output.
        level (str): Tingkat kecerahan ('sangat gelap', 'gelap', 'normal', 'cerah', 'sangat cerah').
