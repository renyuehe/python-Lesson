import os
from setuptools import setup, find_packages

setup(
    name='pytest',#应用名
    version='0.0.3',#版本号
    description='a test package',
    license='GPL Licence',
    author='xuanyu',
    author_email='601612274@qq.com',
    url="./mypack",
    packages=find_packages(exclude=('test*',)),#包括在安装包内的Python包
    include_package_data=True,#启用清单文件MANIFEST.in,包含数据文件
    exclude_package_data = {'docs':['1.txt']},  #排除文件
    python_requires='>=3.6',
    install_requires=['numpy>=1.16.4', 'scipy>=1.3.1', 'xarray>=0.15.0'], #自动安装依赖
    data_files=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Development Status :: 4 - Beta"
    ],
    scripts=[],
)
