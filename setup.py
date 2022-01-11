#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pygame-ext-spritesheets",
    version="1.1",
    description="Maintained version of pygame's spritesheet code. Remade for Python 3.",
    long_description=long_description, 
    author="Pygame Community",
    author_email="pygame@pygame.org",
    maintainer="Double Fractal Studios",
    maintainer_email="pezleha@gmail.com",
    url="https://github.com/DoubleFractal/pygame-ext-spritesheets",
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: pygame"
        
    ],
    packages = ["pygame.ext.spritesheets"],
    install_requires=["pygame>=2.0.1"], 
    project_urls = {
        "Bug Tracker": "https://github.com/DoubleFractal/pygame-ext-spritesheets/issues",
        "Source": "https://github.com/DoubleFractal/pygame-ext-spritesheets",
    },
    
)
