from setuptools import find_packages, setup

setup(
    name="lab3",
    packages=find_packages(exclude=["lab3_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
