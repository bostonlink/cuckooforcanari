# Cuckooforcanari - Cuckoo Sandbox Local Maltego Transforms

Author : David Bressler (@bostonlink)

Demo Video: http://www.youtube.com/watch?v=1GGArfEijgE

## About

Cuckooforcanari is a Maltego local transform project, built within the Canari Framework that integrates the Cuckoo Sandbox API into maltego entity output.  The main goal of this project is to allow security analysts, researchers, investigators, and teams to graphically display a Cuckoo Sandbox file or URL analysis. 

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

### 2.2 - Requirements
cuckooforcanari is supported and tested on Python 2.7.3

The canari framework must be installed to use this package
See: https://github.com/allfro/canari

A Cuckoo Sandbox v0.5 or later local network or host installation and have the Cuckoo API running.
See: http://docs.cuckoosandbox.org/en/latest/usage/api/#starting-the-api-server  

This package depends on the python requests package added requirement to setup.py will automatically download and install the requests package if needed.

### 2.3 - How to install
Once you have the Canari framework installed and working, follow the directions below to install cuckooforcanari

Install the package:

```bash
$ cd cuckooforcanari
$ python setup.py install
```
Then install the canari package by issuing the following:

```bash
$ canari create-profile cuckooforcanari
```
Then do the following (thanks to Nadeem Douba @ndouba):

 INSTRUCTIONS:
 -------------
 1. Open Maltego.
 2. Click on the home button (Maltego icon, top-left corner).
 3. Click on 'Import'.
 4. Click on 'Import Configuration'.
 5. Follow prompts.
 6. Enjoy!

Once installed you must edit the cuckooforcanari.conf file with local environment settings.

```bash
$ vim ~/.canari/cuckooforcanari.conf
```
All Done!!  Have fun!

## Special Thanks!

Rich Popson (@Rastafari0728)  
Nadeem Douba (@ndouba)  
Paterva (@Paterva)  
Cuckoo Sandbox (@cuckoosandbox)  
MassHackers (@MassHackers)  
