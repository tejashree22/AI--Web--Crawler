from setuptools import setup, find_packages

setup(
    name="rufus",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "selenium",
        "webdriver-manager",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "rufus=rufus:main",
        ],
    },
)
