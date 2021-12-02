

from setuptools import setup, find_packages


setup(

    name="mydemo4",
    version="0.1",
    packages=find_packages('src'),  # 包含所有src中的包
    package_dir={'': 'src'},  # 告诉distutils包都在src下

    # 全部打包
    include_package_data = True,

    # 排除所有 README.txt
    exclude_package_data = {'': ['README.txt']},
)
