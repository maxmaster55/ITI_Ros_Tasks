from setuptools import find_packages, setup

package_name = 'task_2_Obstacle_Detection'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'pub_sensor = task_2_Obstacle_Detection.pub_sensor:main',
            'sub_sensor = task_2_Obstacle_Detection.sub_sensor:main',
        ],
    },
)
