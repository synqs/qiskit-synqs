import os
import sys
import setuptools
import inspect

long_description = """Qiskit synqs is for synqs devices."""

with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

VERSION_PATH = os.path.join(os.path.dirname(__file__), "qiskit_synqs", "VERSION.txt")
with open(VERSION_PATH, "r") as version_file:
    VERSION = version_file.read().strip()

setuptools.setup(
    name="qiskit-synqs",
    version=VERSION,
    description="Integration of cold atomic experiments into the Qiskit SDK.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/synqs/qiskit-synqs",
    author="Synqs",
    author_email="darth_vader@synqs.org",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum cold atoms",
    packages=setuptools.find_packages(
        include=["qiskit_synqs", "qiskit_synqs.*"]
    ),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=False,
)
