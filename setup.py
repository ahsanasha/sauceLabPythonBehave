# from distutils.core import setup
from setuptools import setup, find_packages

setup(name='sauceLab web apps',
      version='1.0',
      description='Python BDD with behave',
      url='https://www.saucelab.com/',
      packages= find_packages()
      # packages=[
      #     'BDD_common',
      #     'BDD_common.CommonConf igs',
      #     'BDD_common.common_funcs',
      #     'BDD_common.CommonSteps',
      # ],
      )
