import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dtuprosys",
    version_config=True,
    setup_requires=["setuptools-git-versioning"],
    author="Pau Cabaneros",
    author_email="pau.cabaneros@gmail.com",
    description="Package to teach chemometrics in the context of fermentation processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paucablop/dtu.prosys",
    project_urls={
        "Bug Tracker": "https://github.com/paucablop/dtu.prosys/issues/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.9",
    install_requires=[
        "numpy==1.23.0",
        "pandas==1.4.3",
        "matplotlib==3.5.2",
        "mbpls==1.0.8b1",
        "scipy==1.9.0rc1",
        "scikit-learn==1.1.1",
    ],
    include_package_data=True,
)
