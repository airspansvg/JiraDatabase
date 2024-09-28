from setuptools import setup, find_packages

setup(
    name="JiraDatabase",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    package_data={
        "JiraDatabase": ["**/*.json"],  # Ensure the JSON files are included in the package
    },
    description="JIRA data backup package",
    author="Sitaram Hudda",
    author_email="shudda@airspan.com",
)
