from setuptools import setup, find_packages

setup(
    name='Anu',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Tambahkan dependensi yang diperlukan
        'numpy',      # Contoh dependensi
        'Pillow',     # Untuk pengolahan gambar
    ],
)
