# vim:fileencoding=utf-8:noet

from setuptools import setup

setup(
    name             = 'powerline-kubernetes',
    description      = 'A Powerline segment to show Kubernetes context',
    version          = '1.0.1',
    keywords         = 'powerline kubernetes context',
    license          = 'MIT',
    author           = 'Vincent De Smet',
    author_email     = 'vincent.drl@gmail.com',
    url              = 'https://github.com/so0k/powerline-kubernetes',
    packages         = ['powerline_kubernetes'],
    install_requires = ['powerline-status', 'kubernetes-py'],
    classifiers      = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)
