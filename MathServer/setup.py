import setuptools


with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()


setuptools.setup(
    name="http_math_server",
    version="0.8",
    author="Aleksey",
    author_email="aleksisgreeby@mail.ru",
    description="Example of math server",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages()
)