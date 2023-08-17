from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pybullet_log_reader",
    description="",
    version="0.0.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cmower/pybullet_log_reader",
    project_urls={
        "Bug Tracker": "https://github.com/cmower/pybullet_log_reader/issues",
    },
    author="Christopher E. Mower",
    author_email="",
    license="GNU General Public License v3.0",
    packages=["pybullet_log_reader"],
    install_requires=["pandas"],
)
