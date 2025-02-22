from setuptools import find_packages, setup

setup(
    name="food-delivery-service-api",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
