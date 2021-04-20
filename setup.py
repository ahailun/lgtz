
import setuptools

with open("readme.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="lugang",
    version="0.0.1",
    author="test",
    author_email="test@example.com",
    description="test pip",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)