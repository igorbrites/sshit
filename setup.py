from distutils.core import setup

setup(
    name='sshit',
    packages=['src', 'src.controller', 'sshit'],
    install_requires=['cement', 'pyYaml'],
    version='0.0.2',
    description='SSH Client made simple',
    long_description=open('README.md').read(),
    license='MIT',
    author='Igor Brites',
    author_email='igor.brites.87@gmail.com',
    url='https://github.com/igorbrites/sshit',
    download_url='https://github.com/igorbrites/sshit/archive/0.0.2.tar.gz',
    keywords='ssh cli',
    python_requires='>=3',
    classifiers=[],
    entry_points={
        'console_scripts': [
            'sshit=sshit:main',
        ],
    }
)
