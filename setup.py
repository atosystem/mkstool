from setuptools import setup, find_packages

setup(
    name='mkstool',
    version='1.0.0',
    description='mkstool API',
    long_description=
    ('Official API for https://www.kaggle.com, accessible using a command line '
     'tool implemented in Python. Beta release - Kaggle reserves the right to '
     'modify the API functionality currently offered.'),
    author='Kaggle',
    author_email='support@kaggle.com',
    url='https://github.com/Kaggle/kaggle-api',
    keywords=['Kaggle', 'API'],
    entry_points={'console_scripts': 
        ['mkstool = mkstool.__main__:main']
    },
    install_requires=[
        # Restriction that urllib3's version is less than 1.25 needed to avoid
        # requests dependency problem.
        'urllib3 >= 1.21.1, < 1.25',
        'certifi',
        'python-dateutil',
        'requests',
        'tqdm',
        'python-slugify',
        'Click'
    ],
    packages=find_packages(),
    license='Apache 2.0')