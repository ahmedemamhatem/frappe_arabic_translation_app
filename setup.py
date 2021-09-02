from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in translation_app/__init__.py
from translation_app import __version__ as version

setup(
	name="translation_app",
	version=version,
	description="This app is for translate to Arabic",
	author="Deaa",
	author_email="dmahmoudm@creativeadvtech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
