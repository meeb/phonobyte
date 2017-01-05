from setuptools import (setup, find_packages)
from phonobyte import __version__ as version


setup(
    name='phonobyte',
    version=str(version),
    url='https://github.com/mgrp/phonobyte',
    download_url='https://github.com/mgrp/phonobyte/tarball/0.1',
    author='the m group, https://m.pr/',
    author_email='hi@m.pr',
    description=('Encoding bytes to phonetically pronounceable words. '),
    license='LGPLv3',
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 '
            'or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=('phonobyte',),
    test_suite='tests',
)
