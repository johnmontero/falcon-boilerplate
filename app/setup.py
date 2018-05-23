import api
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
from setuptools import setup, find_packages

long_description = "Api falcon boilerplate"
requirements = parse_requirements('requirements.txt', session=False)
install_requires = [str(r.req) for r in requirements]

setup(
    name             = 'api',
    description      = 'API falcon boilerplate',
    packages         = find_packages(),
    author           = 'John Montero Chunga',
    author_email     = 'jmonteroc [at] gmail.com',
    scripts          = ['bin/api'],
    install_requires = install_requires,
    version          = api.__version__,
    license          = "MIT",
    zip_safe         = False,
    keywords         = "api, falcon, rest",
    long_description = long_description,
    classifiers      = [
                        'Development Status :: 4 - Beta',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: MIT License',
                        'Topic :: Software Development :: Build Tools',
                        'Topic :: Software Development :: Libraries',
                        'Topic :: Software Development :: Testing',
                        'Topic :: Utilities',
                        'Operating System :: MacOS :: MacOS X',
                        'Operating System :: Microsoft :: Windows',
                        'Operating System :: POSIX',
                        'Programming Language :: Python :: 2.6',
                        'Programming Language :: Python :: 2.7',
                      ]
)