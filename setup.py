from setuptools import setup

setup(
    name='myprs',
    version="0.0",

    description="Shows open GitHub PRs across an organisation's repos",
    author="Kristian Glass",
    author_email="myprs@doismellburning.co.uk",
    url="https://github.com/doismellburning/myprs",
    license="MIT",

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
