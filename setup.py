import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


__version__='0.0.0'
REPO_NAME='chicken_deases_classification'
AUTHER_USER_NAME='ZAAK1234'
SRC_REPO='chicken_deases_classification'
AUTHER_EMAIL='fjaragal@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHER_USER_NAME,
    author_email=AUTHER_EMAIL,
    description='A small python package to classify chicken deases',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/{SRC_REPO}/{REPO_NAME}',
    project_urls={
        "Bug Tracker": f'https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)