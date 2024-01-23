from setuptools import setup, find_packages

setup(
    name='quantum_computing_simulator',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    tests_require=[
        'pytest',
        # add other test dependencies here
    ],
)
