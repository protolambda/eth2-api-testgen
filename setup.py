from setuptools import setup, find_packages

with open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="eth2_api_testgen",
    description="Eth2 API test gen",
    version="0.0.1",
    long_description=readme,
    long_description_content_type="text/x-markdown",
    author="protolambda",
    author_email="proto+pip@protolambda.com",
    url="https://github.com/protolambda/eth2-api-testgen",
    python_requires=">=3.8, <4",
    license="MIT",
    packages=find_packages(),
    tests_require=[],
    install_requires=[
        "requests>=2.25.0"
    ],
    include_package_data=True,
    keywords=["eth2", "ethereum", "serenity", "api", "test"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
