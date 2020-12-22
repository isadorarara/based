from setuptools import setup

setup(name='based',
      version='0.1.0',
      description='a base converter, encrypter and compiler',
      author='Y0N1N1 (gabriel)',
      license='MIT',
      packages = ['based'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=['math','os'],
      python_requires='>=3.8',
      extras_require={
        'dev': [
            "math",
            "os"
        ],
      },
      include_package_data=True)
