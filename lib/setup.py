from setuptools import setup
import setuptools

##setuptools.setup(version_config=True, setup_requires=["setuptools-git-versioning"])

setup(name='ppdl',
      install_requires=['matplotlib','numpy', 
                        'progressbar2', 'sympy', 'rlxutils'
                       ],
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      scripts=[],
      packages=['ppdl'],
      include_package_data=True,
      zip_safe=False)
