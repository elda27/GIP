from setuptools import setup
from pathlib import Path

# Get version from main script
__version__ = None

src_dir = Path(__file__).parent.absolute()
version_file = src_dir / 'gip' / 'version.py'
with open(version_file, 'r') as fp:
    exec(fp.read())

fndoc = Path(src_dir) / 'README.md'
with open(fndoc, 'r') as fp:
    README = fp.read()

setup(
    name='gip',
    version=__version__,
    description='Image processing tool for console',
    long_description=README,
    license='MIT Licences',
    url='https://github.com/elda27/gip',
    maintainer='elda27',
    # maintainer_email=None,
    platforms=['any'],
    packages=[
        'gip',
        'gip.args',
        'gip.converters',
        'gip.core',
        'gip.envs',
        'gip.functions',
        'gip.functions.concat',
        'gip.logging',
        'gip.image_utils',
        'gip.third_party',
    ],
    extras_require={},
    entry_points={
        'console_scripts': [
            "gip = gip.main:main"
        ]
    },
    python_requires='>=3.6',
    classifiers=[
        # (https://pypi.org/pypi?%3Aaction=list_classifiers)
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: MS-DOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: SunOS/Solaris',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    # keywords=None,
)
