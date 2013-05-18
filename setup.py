# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages

setup(
    name="jukebox-mpg123",
    packages=find_packages(),
    version="0.1",
    description="mpg123 playback service for jukebox",
    author="Jens Nistler",
    author_email="opensource@jensnistler.de",
    url="http://jensnistler.de/",
    download_url='http://github.com/lociii/jukebox_mpg123',
    keywords=["jukebox", "music", "mp3", "playback", "backend", "mpg123"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Players",
    ],
    install_requires=[
        "jukebox>=0.3.7",
        "python-daemon==1.6",
    ],
    include_package_data=True,
    long_description=open("README.rst").read()
)
