
# from setuptools import setup, find_packages
#
# setup(
#     name = "mydemo2",
#     version = "0.1",
#     packages = find_packages(),
# )

from setuptools import setup, find_packages
setup(
    packages = find_packages('src'),  # 包含所有src中的包
    package_dir = {'':'src'},   # 告诉distutils包都在src下

    package_data = {
        # 任何包中含有.txt文件，都包含它
        '': ['*.txt'],
        # 包含demo包data文件夹中的 *.dat文件
        'mydemo_up': ['data/*.dat'],
    }
)
