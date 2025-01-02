About tpot-feedstock
====================

Feedstock license: [BSD-3-Clause](https://github.com/conda-forge/tpot-feedstock/blob/main/LICENSE.txt)

Home: https://epistasislab.github.io/tpot

Package license: LGPL-3.0-or-later

Summary: A Python tool that automatically creates and optimizes Machine Learning pipelines using genetic programming.


Development: https://github.com/EpistasisLab/tpot

Consider TPOT your Data Science Assistant. TPOT is a Python Automated
Machine Learning tool that optimizes machine learning pipelines using
genetic programming.

TPOT will automate the most tedious part of machine learning by
intelligently exploring thousands of possible pipelines to find the best
one for your data.

Once TPOT is finished searching (or you get tired of waiting), it provides
you with the Python code for the best pipeline it found so you can tinker
with the pipeline from there.

TPOT is built on top of scikit-learn, so all of the code it generates
should look familiar... if you're familiar with scikit-learn, anyway.

TPOT is still under active development and we encourage you to check back
on this repository regularly for updates.


Current build status
====================


<table><tr><td>All platforms:</td>
    <td>
      <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=2089&branchName=main">
        <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/tpot-feedstock?branchName=main">
      </a>
    </td>
  </tr>
</table>

Current release info
====================

| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-tpot-green.svg)](https://anaconda.org/conda-forge/tpot) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/tpot.svg)](https://anaconda.org/conda-forge/tpot) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/tpot.svg)](https://anaconda.org/conda-forge/tpot) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/tpot.svg)](https://anaconda.org/conda-forge/tpot) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-tpot--dask-green.svg)](https://anaconda.org/conda-forge/tpot-dask) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/tpot-dask.svg)](https://anaconda.org/conda-forge/tpot-dask) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/tpot-dask.svg)](https://anaconda.org/conda-forge/tpot-dask) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/tpot-dask.svg)](https://anaconda.org/conda-forge/tpot-dask) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-tpot--full-green.svg)](https://anaconda.org/conda-forge/tpot-full) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/tpot-full.svg)](https://anaconda.org/conda-forge/tpot-full) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/tpot-full.svg)](https://anaconda.org/conda-forge/tpot-full) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/tpot-full.svg)](https://anaconda.org/conda-forge/tpot-full) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-tpot--imblearn-green.svg)](https://anaconda.org/conda-forge/tpot-imblearn) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/tpot-imblearn.svg)](https://anaconda.org/conda-forge/tpot-imblearn) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/tpot-imblearn.svg)](https://anaconda.org/conda-forge/tpot-imblearn) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/tpot-imblearn.svg)](https://anaconda.org/conda-forge/tpot-imblearn) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-tpot--mdr-green.svg)](https://anaconda.org/conda-forge/tpot-mdr) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/tpot-mdr.svg)](https://anaconda.org/conda-forge/tpot-mdr) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/tpot-mdr.svg)](https://anaconda.org/conda-forge/tpot-mdr) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/tpot-mdr.svg)](https://anaconda.org/conda-forge/tpot-mdr) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-tpot--skrebate-green.svg)](https://anaconda.org/conda-forge/tpot-skrebate) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/tpot-skrebate.svg)](https://anaconda.org/conda-forge/tpot-skrebate) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/tpot-skrebate.svg)](https://anaconda.org/conda-forge/tpot-skrebate) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/tpot-skrebate.svg)](https://anaconda.org/conda-forge/tpot-skrebate) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-tpot--torch-green.svg)](https://anaconda.org/conda-forge/tpot-torch) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/tpot-torch.svg)](https://anaconda.org/conda-forge/tpot-torch) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/tpot-torch.svg)](https://anaconda.org/conda-forge/tpot-torch) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/tpot-torch.svg)](https://anaconda.org/conda-forge/tpot-torch) |

Installing tpot
===============

Installing `tpot` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Once the `conda-forge` channel has been enabled, `tpot, tpot-dask, tpot-full, tpot-imblearn, tpot-mdr, tpot-skrebate, tpot-torch` can be installed with `conda`:

```
conda install tpot tpot-dask tpot-full tpot-imblearn tpot-mdr tpot-skrebate tpot-torch
```

or with `mamba`:

```
mamba install tpot tpot-dask tpot-full tpot-imblearn tpot-mdr tpot-skrebate tpot-torch
```

It is possible to list all of the versions of `tpot` available on your platform with `conda`:

```
conda search tpot --channel conda-forge
```

or with `mamba`:

```
mamba search tpot --channel conda-forge
```

Alternatively, `mamba repoquery` may provide more information:

```
# Search all versions available on your platform:
mamba repoquery search tpot --channel conda-forge

# List packages depending on `tpot`:
mamba repoquery whoneeds tpot --channel conda-forge

# List dependencies of `tpot`:
mamba repoquery depends tpot --channel conda-forge
```


About conda-forge
=================

[![Powered by
NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org)

conda-forge is a community-led conda channel of installable packages.
In order to provide high-quality builds, the process has been automated into the
conda-forge GitHub organization. The conda-forge organization contains one repository
for each of the installable packages. Such a repository is known as a *feedstock*.

A feedstock is made up of a conda recipe (the instructions on what and how to build
the package) and the necessary configurations for automatic building using freely
available continuous integration services. Thanks to the awesome service provided by
[Azure](https://azure.microsoft.com/en-us/services/devops/), [GitHub](https://github.com/),
[CircleCI](https://circleci.com/), [AppVeyor](https://www.appveyor.com/),
[Drone](https://cloud.drone.io/welcome), and [TravisCI](https://travis-ci.com/)
it is possible to build and upload installable packages to the
[conda-forge](https://anaconda.org/conda-forge) [anaconda.org](https://anaconda.org/)
channel for Linux, Windows and OSX respectively.

To manage the continuous integration and simplify feedstock maintenance
[conda-smithy](https://github.com/conda-forge/conda-smithy) has been developed.
Using the ``conda-forge.yml`` within this repository, it is possible to re-render all of
this feedstock's supporting files (e.g. the CI configuration files) with ``conda smithy rerender``.

For more information please check the [conda-forge documentation](https://conda-forge.org/docs/).

Terminology
===========

**feedstock** - the conda recipe (raw material), supporting scripts and CI configuration.

**conda-smithy** - the tool which helps orchestrate the feedstock.
                   Its primary use is in the construction of the CI ``.yml`` files
                   and simplify the management of *many* feedstocks.

**conda-forge** - the place where the feedstock and smithy live and work to
                  produce the finished article (built conda distributions)


Updating tpot-feedstock
=======================

If you would like to improve the tpot recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`conda-forge` channel, whereupon the built conda packages will be available for
everybody to install and use from the `conda-forge` channel.
Note that all branches in the conda-forge/tpot-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string)
   back to 0.

Feedstock Maintainers
=====================

* [@bollwyvl](https://github.com/bollwyvl/)
* [@jay-m-dev](https://github.com/jay-m-dev/)
* [@proinsias](https://github.com/proinsias/)

