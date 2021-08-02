import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-easy-rest-mongo-motor-repo",
    version="0.1.0",
    author="Jean Pinzon",
    author_email="jean.pinzon1@gmail.com",
    description="Mongo repo to use with Py Easy REST",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(
        exclude=(
            'tests',
        ),
    ),
    install_requires=[
        "motor==2.3.0",
    ],
    extras_require={
        'tests': [
            "coverage==5.5",
            "pytest==6.1.2",
            "pytest-asyncio==0.14.0",
            "pytest-cov==2.10.1",
            "flake8==3.8.4",
            "aiounittest==1.4.0",
            "twine==3.3.0",
            "build==0.3.1.post1",
        ],
    },
    python_requires='>=3.8',
)
