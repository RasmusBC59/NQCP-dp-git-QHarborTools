# qharbortools
<p align="center">
  <img src="https://img.shields.io/static/v1?style=for-the-badge&label=code-status&message=Good&color=green"/>
  <img src="https://img.shields.io/static/v1?style=for-the-badge&label=initial-commit&message=Rasmus Bjerregaard Christensen&color=inactive"/>
    <img src="https://img.shields.io/static/v1?style=for-the-badge&label=maintainer&message=NQCP&color=inactive"/>
</p>



# Description
[Examples](https://nqcp.github.io/NQCP-dp-git-qharbortools/example_notebooks/index.html)
# Installation
You can install `qharbortools` from the [NQCP package feed](https://dev.azure.com/NQCP/NQCP/_wiki/wikis/NQCP.wiki/375/Installing-NQCP-Packages) using pip. 

```bash
$ pip install qharbortools
```
# Usage

## Running the tests

If you have gotten 'qharbortools' from source, you may run the tests locally.

Install `qharbortools` along with its test dependencies into your virtual environment by executing the following in the root folder

```bash
$ pip install .[test]
```

Then run `pytest` in the `tests` folder.

## Building the documentation

If you have gotten `qharbortools` from source, you may build the docs locally.

Install `qharbortools` along with its documentation dependencies into your virtual environment by executing the following in the root folder

```bash
$ pip install .[docs]
```

You also need to install `pandoc`. If you are using `conda`, that can be achieved by

```bash
$ conda install pandoc
```
else, see [here](https://pandoc.org/installing.html) for pandoc's installation instructions.

Then run `make html` (or .\make.bat html on windows) in the `docs` folder. The next time you build the documentation, remember to run `make clean` before you run `make html`.
