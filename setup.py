import io
import os

from setuptools import setup, find_packages

NAME = 'pulse-rest'
DESCRIPTION = 'Python REST API Client for Pulse Robotic Arm '
URL = 'https://rozum.com'
EMAIL = 'ilya.grozov@rozum.com'
AUTHOR = 'Ilya Grozov'
VERSION = '1.4.3.dev0'

if 'dev' in VERSION:
    DEVELOPMENT_STATUS = 'Development Status :: 4 - Beta'
else:
    DEVELOPMENT_STATUS = 'Development Status :: 5 - Production/Stable'

REQUIRED = [
    'certifi >= 14.05.14',
    'six >= 1.10',
    'python_dateutil >= 2.5.3',
    'urllib3 >= 1.15.1',
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    install_requires=REQUIRED,
    url=URL,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        DEVELOPMENT_STATUS,
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    zip_safe=False
)
