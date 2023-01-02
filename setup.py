from setuptools import setup, find_packages


with open('README.md','r',encoding='utf-8') as f:
    long_descriptions = f.read()

setup (
    
    name="zyc_love",
    version="1.0.1",
    author="renaissance",
    author_email="renaissance3310@163.com",
    description=" Code of Love ",
    long_description = long_descriptions,
    long_description_content_type="text/markdown",
    url="https://github.com/renaissancezyc/zyc-love",
    packages=find_packages(),
    classifiers=[                                       
        "Programming Language :: Python :: 3",             
        "License :: OSI Approved :: Apache Software License",   
        "Operating System :: OS Independent",              
    ],

)





