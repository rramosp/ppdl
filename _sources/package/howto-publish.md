# Using setuptools

Make sure your repo is commited, tagged with the new version number and pushed.
For instance:

```sh
git add 
git commit -m message
git tag 0.1.3 # my new version
git push
git push origin 0.1.3
```

To verify the version with which the code will be published, and FIND OUT
THE NEXT VERSION YOU MUST TAG:

```sh
./ppdl/bin/get_scm_version
```

To package and publish your code into pypi:

```sh
rm -rf dist/*
python setup.py sdist
twine upload dist/*
```

If you have not tagged or commited your repo, the version on the package created
by setup tools might be:

local changes not committed              0.25.dev0+g73731b3.d20220113
local changes committed (pushed or not)  0.25.dev1+g3ec6e04

with "0.24" being the last known tag. note the automatic version increment
see: https://pythonrepo.com/repo/pypa-setuptools_scm-python-build-tools

In this case, you would ADD A TAG 0.25, as explained above.

git commands to manage tags:

```sh
git tag 0.1.2 # create tag locally
git push origin 0.1.2 # push tag to repo
git tag -d 0.1.2 # delete tag locally
git push --delete origin 0.1.2 # delete tag in repo
```

# Using poetry

Setup the project version to git version:

```sh
poetry version $(git describe --tags --abbrev=0)
```

Build the project:

```sh
poetry build -f sdist
```

Publish the project

```sh
poetry publish -r juselara-jfrog # change to pypi server for prod
```
