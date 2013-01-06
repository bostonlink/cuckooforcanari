# Cuckooforcanari - Cuckoo Sandbox Local Maltego Transforms

Author : David Bressler (@bostonlink)

## About

Cuckooforcanari is a Maltego local transform project, built within the Canari Framework that integrates the Cuckoo Sandbox v0.5 API into maltego entity output.  The main goal of this project is to allow security analysts, researchers, investigators, and teams to graphically display a Cuckoo Sandbox file analysis. 

Directory Structure:

* `src/cuckooforcanari` directory is where all the magic stuff goes and happens.
* `src/cuckooforcanari/transforms` directory is where all the transform modules are located.
* `src/cuckooforcanari/transforms/common` directory is where common code for all transforms are stored.
* `src/cuckooforcanari/transforms/common/entities.py` is where custom entities are defined.
* `maltego/` is where the Maltego entity exports are stored.
* `src/cuckooforcanari/resources/maltego` directory is where the `entities.mtz` and `*.machine` files are stored for auto install and uninstall.

## 2.0 - Installation

### 2.1 - Supported Platforms
cuckooforcanari has currently been tested on Mac OS X and Linux.
Further testing will be done on Windows in the near future.

### 2.2 - Requirements
cuckooforcanari is supported and tested on Python 2.7.3

The canari framework must be installed to use this package
See: https://github.com/allfro/canari

This package depends on the python requests package (added requirements source into the project)

### 2.3 - How to install
Once you have the Canari framework installed and working, follow the directions below to install cuckooforcanari

Install the package:

```bash
$ cd cuckooforcanari
$ python setup.py install
```
Then install the canari package by issuing the following:

```bash
$ canari install-package cuckooforcanari
```
Once installed you must edit the cuckooforcanari.conf file with local environment settings.

```bash
$ vim cuckooforcanari/cuckooforcanari.conf
```
All Done!!  Have fun!

## Special Thanks!

* Rich Popson (@Rastafari0728)<br/>
* Nadeem Douba (@ndouba)<br/>
* Paterva (@Paterva)<br/>
* Cuckoo Sandbox (@cuckoosandbox)
* MassHackers (@MassHackers)<br/>