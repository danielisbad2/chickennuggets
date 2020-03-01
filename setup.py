from setuptools import setup, find_packages
from os import path


# Read long description from README.md
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()


setup(
    name='chickennuggets',
    use_scm_version=True,

    description='Utility cogs for Discord.py bots',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Daniel Thwaites',
    author_email='danthwaites30@btinternet.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='Discord utilities',

    url='https://github.com/AlphaMycelium/chickennuggets',
    project_urls={
        'Bug Reports': 'https://github.com/AlphaMycelium/chickennuggets/issues',
        'Source': 'https://github.com/AlphaMycelium/chickennuggets',
    },

    packages=find_packages(),
    python_requires='>=3.6,<4',
    setup_requires=['setuptools_scm'],
    install_requires=['discord.py >=1.2.5,<2']
)
