from setuptools import setup

package_name = 'vr_connector'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zpw',
    maintainer_email='zpw@gmail.com',
    description='This package is to exchange information with VR devices',
    license='Siemens Robotics Team',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = vr_connector.vr_talker:main',
            'listener = vr_connector.vr_receiver:main',
        ],
    },
)
