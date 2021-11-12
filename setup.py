import setuptools
import bili_uploader

with open("README.md", "rt", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="bili_uploader",
    version=bili_uploader.__version__,
    author="Brx86",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Brx86/bilibili-picpool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)