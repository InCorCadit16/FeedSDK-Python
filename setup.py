from setuptools import setup, find_packages

setup(
    name='feed-sdk',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "pandas",
        "urllib3",
        "certifi",
        "aenum",
        "SQLAlchemy"
    ],
    author='eBay',
    description='Python SDK for accessing eBay Feed API',
    url='https://github.com/InCorCadit16/FeedSDK-Python.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
