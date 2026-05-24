from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'task_5_csv_playback'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'data'),
         glob('task_5_csv_playback/data/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='maxmaster',
    maintainer_email='yousseflkashef000@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'csv_playback = task_5_csv_playback.csv_playback:main'
        ],
    },
)
