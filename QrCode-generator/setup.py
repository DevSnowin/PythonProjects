from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
        name="QR_Maker",
        version="1.0.0",
        description="Paste your text and links and get as a QR code!",
        long_description=long_description,
        author="Snowin",
        license="MIT",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Shopkeepers",
            "License :: OSI Approved :: MIT License"
        ],
        keywords="qr code generator",
        packages=find_packages(),
        install_requires=["requests>=2"],
        python_requires="~=3.5"
    )
