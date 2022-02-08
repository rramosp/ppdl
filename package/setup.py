from setuptools import setup

# requirements
with open("requirements.txt") as f:
    requirements = f.readlines()

setup(
        name="ppdl",
        install_requires=requirements,
        use_scm_version={"root": "../"},
        setup_requires=["setuptools_scm"],
        scripts=[],
        packages=["ppdl"],
        include_package_data=True,
        zip_safe=False
        )
