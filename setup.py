from setuptools import setup

setup(
    name='py2neo',
    version='4.3.0',
    description='A Python driver for Neo4j',
    author='Neo4j, Inc.',
    author_email='info@neo4j.com',
    url='https://github.com/neo4j/py2neo',
    license='Apache Software License',
    install_requires=[
        'neobolt>=1.7.13,<1.8.0',
        'neotime>=1.7.4,<1.8.0',
        'validators>=0.14.0,<0.15.0',
        'urllib3<1.25,>=1.23',
    ],
    extras_require={
        'docs': [
            'sphinx>=1.8.5,<2.0.0',
            'sphinx-rtd-theme>=0.5.0,<0.6.0',
            'sphinxcontrib-napoleon>=0.6.2,<0.7.0',
        ],
        'tests': [
            'pytest>=6.2.4,<7.0.0',
            'pytest-cov>=2.10.1,<3.0.0',
            'pytest-neo4j>=5.1.0,<6.0.0',
            'flake8>=3.9.2,<4.0.0',
            'mypy>=0.931,<0.940',
            'coveralls>=3.2.0,<4.0.0',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
