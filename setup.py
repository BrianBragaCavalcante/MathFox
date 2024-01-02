from setuptools import setup
import os

pastas = ['mathfox', 'mathfox.numis', 'mathfox.number', 'mathfox.cal', 'mathfox.cal.geo', 'mathfox.cal.geo.trigo',
          'mathfox.cal.geo.area', 'mathfox.cal.geo.area.two_dimensions', 'mathfox.cal.geo.area.three_dimensions']

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='mathfox',
      version='1.1.2b1',
      license='MIT License',
      author='Brian Braga Cavalcante',
      long_description=readme,
      long_description_content_type="text/markdown",
      author_email='brianbragacavalcantex@gmail.com',
      keywords='math',
      description=u'A library with math functions to help Python developers with their projects.',
      packages=pastas,
      package_data={'': ['DOCUMENTATION.md', 'README.md']},
      include_package_data=True,
      python_requires='>=3.6',
      )
