[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
description = "Paket Python untuk pengolahan gambar"
authors = [
    { name = "Nama Anda", email = "email@anda.com" }
]
license = { text = "MIT" }
readme = "README.md"
homepage = "https://github.com/Jeanjrg/Project-kelompok-3B-algoritma"
repository = "https://github.com/Jeanjrg/Project-kelompok-3B-algoritma"
keywords = ["gambar", "pengolahan", "python"]

[project.dependencies]
numpy = "^1.21"
Pillow = "^8.0"

[tool.setuptools.packages.find]
where = ["my_package"]  # Pastikan 'my_package' adalah nama direktori yang sesuai
