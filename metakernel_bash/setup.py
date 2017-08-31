from setuptools import setup


setup(name='metakernel_bash',
      version_format='0.19.1.dev{commitcount}+{gitsha}',
      description='A Bash kernel for Jupyter/IPython',
      long_description='A Bash kernel for Jupyter/IPython, based on MetaKernel',
      url='https://github.com/calysto/metakernel/tree/master/metakernel_bash',
      author='Steven Silvester',
      author_email='steven.silvester@ieee.org',
      py_modules=['metakernel_bash'],
      install_requires=['metakernel'],
      setup_requires=['setuptools-git-version'],
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
          'Topic :: System :: Shells',
      ]
)
