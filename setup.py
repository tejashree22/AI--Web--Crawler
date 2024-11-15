from setuptools import setup, find_packages

setup(
    name="rufus",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "selenium",
        "webdriver-manager"
    ],
    entry_points={
        "console_scripts": [
            "rufus=rufus_client:main",
        ],
    },
    description="Rufus: AI-powered web scraping tool for RAG pipelines.",
    author="Your Name",
    author_email="your_email@example.com",
)
