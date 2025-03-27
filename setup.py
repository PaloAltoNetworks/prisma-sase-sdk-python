from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='prisma_sase',
      version='6.5.2b2',
      description='Python3 SDK for the Prisma SASE AppFabric',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/PaloAltoNetworks/prisma-sase-sdk-python',
      author='Prisma SASE Developer Support',
      author_email='prisma-sase-developers@paloaltonetworks.com',
      license='MIT',
      install_requires=[
            'requests',
            'websockets >= 8.1; python_version > "3.6"',
            'urllib3 >= 2.0.0'
      ],
      packages=['prisma_sase'],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "Programming Language :: Python :: 3.12",
      ]
      )
