from setuptools import setup, find_packages


setup(
    name = "mydemo3",
    version = "0.1",
    packages = find_packages('src'), # 包含所有src中的包
    package_dir = {'': 'src'},  # 告诉distutils包都在src下

    entry_points={
        'console_scripts': [
            'foo = demo:test',
            'bar = demo:test',
        ],
        'gui_scripts': [
            'baz = demo:test',
        ]
    }
)
