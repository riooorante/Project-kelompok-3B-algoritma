from PIL import Image, ImageOps

def flip_image(image_path,output_path,direction):
    """
    Memantulkan gambar baik secara horizontal atau vertikal.

    :param image_path: Path ke file gambar yang ingin dipantulkan.
    :param output_path: Path untuk menyimpan gambar yang dipantulkan.
    :param direction: Arah pemantulan ('horizontal' atau 'vertical').
    """
    try:
        # Buka gambar
        image = Image.open(image_path)

        # Pemantulan gambar sesuai arah
        if direction == 'horizontal':
            flipped_image = ImageOps.mirror(image)
        elif direction == 'vertikal':
            flipped_image = ImageOps.flip(image)
        else:
            raise ValueError("Arah yang dimasukkan harus 'horizontal' atau 'vertikal'.")

        # Simpan gambar yang dipantulkan
        flipped_image.save(output_path)
        return f"Gambar berhasil dipantulkan dan disimpan di: {output_path}"
        flipped_image.show()
    except Exception as e:
        return f"Terjadi kesalahan: {e}"
