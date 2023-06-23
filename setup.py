from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='prisma-sase',
      version='6.2.2b1',
      description='Python2 and Python3 SDK for the Prisma SASE AppFabric',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/PaloAltoNetworks/prisma-sase-sdk-python',
      author='Prisma SASE Developer Support',
      author_email='prisma-sase-developers@paloaltonetworks.com',
      license='MIT',
      install_requires=[
            'requests[security] >= 2.22.0',
            'websockets >= 8.1; python_version >= "3.6"',
            'urllib3 == 1.26.16'
      ],
      packages=['prisma_sase'],
      classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
      ]
      )
