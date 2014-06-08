try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='DAPIWrap',
    version='0.1.0',
    author='Alex Crawford',
    author_email='trebek604@gmail.com',
    packages=['dapiwrap'],
    scripts=[],
    url='https://github.com/Trebek/DAPIWrap',
    license='LICENSE.txt',
    description='A wrapper for the Doomworld /idgames archive API.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Internet'
    ],
    keywords='Doomworld idgames archive API Wrapper interface',
    install_requires=[
        "requests"
    ],
    include_package_data=True,
    zip_safe=False
)