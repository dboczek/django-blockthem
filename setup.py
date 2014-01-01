from setuptools import setup, find_packages
import os
import blockthem


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Daniel Boczek",
    author_email="daniel.boczek@gmail.com",
    name='django-blockthem',
    version=blockthem.__version__,
    description='App for blocking access to site by IP or UserAgent',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/dboczek/django-blockthem',
    license='Public Domain',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.4',
    ],
    # tests_require=[
    # ],
    packages=find_packages(exclude=["project", "project.*"]),
    include_package_data=True,
    zip_safe=False,
    # test_suite='runtests.main',
)
