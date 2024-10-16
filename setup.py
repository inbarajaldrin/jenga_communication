from setuptools import setup
from glob import glob
import os

package_name = 'jenga_communication'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('lib', package_name), glob('scripts/*.py'))  # Use glob to install scripts
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aaugus11',
    maintainer_email='aaugus11@asu.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'send_jenga_coords = send_jenga_coords:main',
            'simulate_jenga_blocks = simulate_jenga_blocks:main',
            'receive_jenga_coords = receive_jenga_coords:main',
        ],
    },
)
