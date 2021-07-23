from setuptools import setup, find_packages

setup(
    name='sjbbs',
    version='1.0',
    packages=[
        'src',
        'src/db_op'
    ],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_cors'
    ],
    zip_safe=False
)