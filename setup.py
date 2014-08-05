from setuptools import setup, find_packages

setup(
    name='myprs',
    version="0.0",

    description="Shows open GitHub PRs across an organisation's repos",
    author="Kristian Glass",
    author_email="myprs@doismellburning.co.uk",
    url="https://github.com/doismellburning/myprs",
    license="MIT",

    install_requires=(
        "github3.py==0.8.2",
        "requests==2.2.1",
        "uritemplate.py==0.3.0",
        "wsgiref==0.1.2",
    ),

    packages=find_packages(".", exclude=("*.tests", "*.tests.*", "tests.*", "tests")),
    entry_points={
        "console_scripts": (
            "myprs = myprs:main",
        ),
    },

    classifiers=(
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ),
)
