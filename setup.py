from setuptools import setup, find_packages

setup(
    name='APIFetch',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/goldentg/APIFetch',
    license='GPL-3.0',
    author='goldentg',
    author_email='evan.norman@me.com',
    description='A small customizable CLI tool to graphically display various API information within the command line',
    install_requires=[
        'rich',
        'requests',
        'setuptools'
    ],
    entry_points={
        'console_scripts': [
            'apifetch=Main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)