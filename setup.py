#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="django-oauth-toolkit",
    version="1.1.0-hacked",
    url="https://github.com/jazzband/django-oauth-toolkit",

    author="Federico Frenguelli, Massimiliano Pippi",
    author_email="synasius@gmail.com",

    description="OAuth2 Provider for Django",
    long_description="OAuth2 Provider for Django",

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        "django>=1.10",
        "oauthlib>=2.0.3",
        "requests>=2.13.0",
    ],

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
