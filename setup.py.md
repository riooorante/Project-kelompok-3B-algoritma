from setuptools import setup, find_packages

setup(
    name='project-editing-gambar',  # Use hyphens instead of spaces
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Make sure Pillow is installed
    ],
    description=(
        'A package for image editing that includes functionalities '
        'for converting images to grayscale, rotating images, '
        'adjusting brightness, adding text, flipping images, and '
        'cropping images.'
    ),
    author='Nama Anda',  # Replace with your name
    author_email='email@jeanbumbungan@gmail.com',  # Replace with your email
    url='https://github.com/Jeanjrg/Project-kelompok-3B-algoritma.git',  # Replace with the appropriate repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11.9',  # Adjust according to the required Python version
)
