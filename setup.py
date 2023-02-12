from setuptools import setup

setup(name='cbpi4_GPIOInputActor',
      version='0.0.1',
      description='CraftBeerPi Plugin that uses GPIO Input, for switches and buttons',
      author='Mike Rotskoff',
      author_email='mrotskoff@gmail.com',
      url='',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4_GPIOInputActor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4_GPIOInputActor'],
     )