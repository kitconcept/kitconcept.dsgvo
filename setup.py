"""Installer for the kitconcept.dsgvo package."""
from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.md").read(),
        open("CHANGELOG.md").read(),
    ]
)


setup(
    name="kitconcept.dsgvo",
    version="2.0.1",
    description="DSGVO / GDPR compliance for Plone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: Web Environment",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone DSVGO GDPR",
    author="kitconcept GmbH",
    author_email="info@kitconcept.com",
    url="https://pypi.python.org/pypi/kitconcept.dsgvo",
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["kitconcept"],
    package_dir={"": "src"},
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "plone.api",
        "Products.CMFPlone",
        "setuptools",
        "z3c.jbot",
        "plone.app.z3cform",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.testing",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
            "collective.mailchimp",
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
