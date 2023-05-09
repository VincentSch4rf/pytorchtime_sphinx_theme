from setuptools import setup

from pytorchtime_sphinx_theme import __version__

setup(
    name = 'pytorchtime_sphinx_theme',
    version =__version__,
    author = 'Vincent Scharf',
    author_email= 'info@shiftlabny.com',
    url="https://github.com/VincentSch4rf/pytorchtime_sphinx_theme",
    docs_url="https://github.com/VincentSch4rf/pytorchtime_sphinx_theme",
    description='PyTorchTime Sphinx Theme',
    py_modules = ['pytorchtime_sphinx_theme'],
    packages = ['pytorchtime_sphinx_theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={'pytorchtime_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/js/vendor/*.js',
        'static/fonts/FreightSans/*.*',
        'static/fonts/IBMPlexMono/*.*',
        'static/images/*.*',
        'theme_variables.jinja'
    ]},
    entry_points = {
        'sphinx.html_themes': [
            'pytorchtime_sphinx_theme = pytorchtime_sphinx_theme',
        ]
    },
    license= 'MIT License',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
    install_requires=[
       'sphinx'
    ]
)
