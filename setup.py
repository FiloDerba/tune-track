from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = [
    'dependency_injector',
    'python-dotenv==0.19.2',
    'altair==5.5.0',
    'jupyterlab',
    'narwhals==1.33.0',
    'numpy==2.2.0',
    'pandas==2.2.3',
    'plotly==6.0.1',
    'polars==1.26.0',
    'scikit-learn==1.6.1',
    'vegafusion[embed]>=1.5.0',
    "vl-convert-python>=1.6.0",
    "hmmlearn"
]

linting_requires = [
    'flake8==4.0.1',
    'isort==5.10.1',
]

testing_requires = [
    'pytest',
    'pytest-cov',
    'freezegun',
    'pre-commit',
]

setup(
    name='Tune Track',
    version='1.3.0',
    install_requires=requires,
    extras_require={
        'linting': linting_requires,
        'testing': testing_requires,
    },
    # TODO: change name in target repo
    description='This is a repo to analyze user journey',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    # entry_points={
    #     'main': ['main=tune-track.main:main'],
    # }
)
