from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

##edit below function parameters as per your project requirements
REPO_NAME = "E2E-Book-recommender-system"
AUTHOR_USER_NAME = "INNOCENT AMOS MCHECHESI"
SRC_REPO = "book_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small local package for Book Recommendation System",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url='https://github.com/InnocentMchechesi/E2E-Book-recommender-system',
    author_email="mchechesia@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.10",
    install_requires=LIST_OF_REQUIREMENTS
)