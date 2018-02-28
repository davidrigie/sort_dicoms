from setuptools import setup

setup(      name='sort_dicoms',
            version='0.1',
            description='sort dicoms',
            author='David Rigie',
            license='MIT',
            packages=['sort_dicoms'],
            entry_points = {
                  'console_scripts': ['sort_dicoms=sort_dicoms.command_line:main'],
            },
            zip_safe=False,
            install_requires=[
                  'pydicom',
                  ]
      )