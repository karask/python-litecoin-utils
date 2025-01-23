from setuptools import setup
from litecoinutils import __version__

#with open('requirements.txt') as f:
#    requirements = f.read().splitlines()

#install_reqs = parse_requirements('requirements.txt', session=False)
#requirements = [str(ir.req) for ir in install_reqs]

with open('README.rst') as readme:
    long_description = readme.read()

setup(name='litecoin-utils',
      version=__version__,
      description='Litecoin utility functions',
      long_description=long_description,
      author='Konstantinos Karasavvas',
      author_email='kkarasavvas@gmail.com',
      url='https://github.com/karask/python-litecoin-utils',
      license='AGPLv3',
      keywords='litecoin library utilities tools',
      install_requires=[
          'base58check==1.0.2',
          'ecdsa==0.19.0',
          'sympy==1.3',
          'python-bitcoinrpc==1.0'
      ],
      packages=['litecoinutils'],
      #package_data={
      #    'litecoinutils': ['requirements.txt']
      #},
      #include_package_data=True,
      zip_safe=False
     )

