from setuptools import setup

setup(
    name="example",
    version="0.1",
    author="Bhishan Poudel",
    author_email="bp959314@ohio.edu",
    url = "https://github.com/bhishanpdl/example",
    packages=["example"],
    description="Example Project",
    long_description=open("README.md").read(),
    package_data={"": ["README.md", "LICENSE"]},
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    install_requires=["matplotlib", "numpy", "pathos", "scipy", "sklearn"]
)
