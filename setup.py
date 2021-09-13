from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_arabic_translation_app/__init__.py
from frappe_arabic_translation_app import __version__ as version

setup(
	name="frappe_arabic_translation_app",
	version=version,
	description="Application to translate frappe to arabic",
	author="Deaa",
	author_email="dmahmoudm@creativeadvtech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
