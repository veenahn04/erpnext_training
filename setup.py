from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_training/__init__.py
from frappe_training import __version__ as version

setup(
	name="frappe_training",
	version=version,
	description="frappe_training",
	author="veena",
	author_email="veenahn04@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
