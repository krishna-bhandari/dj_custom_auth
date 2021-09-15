import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dj-custom-auth",
    version="0.1",
    author="Krishna Bhandari",
    author_email="krishnabhandaribabu@gmail.com",
    description="A Django app to create custom user types and their roles.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krishna-bhandari/dj_custom_auth/tree/main",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)