About tpot
==========

Home: https://rhiever.github.io/tpot/

Package license: GPL-3.0

Feedstock license: BSD 3-Clause

Summary: A Python tool that automatically creates and optimizes Machine Learning pipelines using genetic programming.

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

All platforms: [![Circle CI](https://circleci.com/gh/conda-forge/tpot-feedstock.svg?style=shield)](https://circleci.com/gh/conda-forge/tpot-feedstock)

Current release info
====================
Version: [![Anaconda-Server Badge](https://anaconda.org/conda-forge/tpot/badges/version.svg)](https://anaconda.org/conda-forge/tpot)
Downloads: [![Anaconda-Server Badge](https://anaconda.org/conda-forge/tpot/badges/downloads.svg)](https://anaconda.org/conda-forge/tpot)

Installing tpot
===============

Installing `tpot` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with:

```
conda config --add channels conda-forge
```

Once the `conda-forge` channel has been enabled, `tpot` can be installed with:

```
conda install tpot
```

It is possible to list all of the versions of `tpot` available on your platform with:

```
conda search tpot --channel conda-forge
```


About conda-forge
=================

conda-forge is a community-led conda channel of installable packages.
In order to provide high-quality builds, the process has been automated into the
conda-forge GitHub organization. The conda-forge organization contains one repository
for each of the installable packages. Such a repository is known as a *feedstock*.

A feedstock is made up of a conda recipe (the instructions on what and how to build
the package) and the necessary configurations for automatic building using freely
available continuous integration services. Thanks to the awesome service provided by
[CircleCI](https://circleci.com/), [AppVeyor](http://www.appveyor.com/)
and [TravisCI](https://travis-ci.org/) it is possible to build and upload installable
packages to the [conda-forge](https://anaconda.org/conda-forge)
[Anaconda-Cloud](http://docs.anaconda.org/) channel for Linux, Windows and OSX respectively.

To manage the continuous integration and simplify feedstock maintenance
[conda-smithy](http://github.com/conda-forge/conda-smithy) has been developed.
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
   the [``build/number``](http://conda.pydata.org/docs/building/meta-yaml.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](http://conda.pydata.org/docs/building/meta-yaml.html#build-number-and-string)
   back to 0.