from setuptools import setup, find_packages

setup(
    name='gankboard',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',  # Pour exposer l'API REST
        'requests'  # Pour faire des appels HTTP externes si nécessaire
    ],
    description='GankBoard API pour la gestion des objets',
    author='Mr. Fremont',
    author_email='votre.email@example.com',
    url='https://votreurl.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
