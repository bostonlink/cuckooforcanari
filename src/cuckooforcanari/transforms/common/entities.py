#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField

__author__ = 'bostonlink'
__copyright__ = 'Copyright 2013, Cuckooforcanari Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'bostonlink'
__email__ = 'bostonlink@pentest-labs.org'
__status__ = 'Development'

__all__ = [
    'CuckooEntity',
    'CuckooTaskID',
    'CuckooSig',
    'CuckooDropped',
    'CuckooMalwareFilename',
    'CuckooHash',
    'CuckooVT',
    'CuckooYara',
    'CuckooMutex',
    'CuckooProcess',
    'CuckooMalwareSample',
    'FileDetails',
    'SignatureAnalysis',
    'NetworkAnalysis',
    'StaticAnalysis',
    'DroppedFiles',
    'BehaviorAnalysis',
    'Processes'

]

@EntityField(name='taskid', propname='taskid', displayname='Task ID')
class CuckooEntity(Entity):
    namespace = 'cuckoo'

@EntityField(name='filename', propname='filename', displayname='Filename')
@EntityField(name='status', propname='status', displayname='Status')
class CuckooTaskID(CuckooEntity):
    pass

class CuckooSig(CuckooEntity):
    pass

@EntityField(name='ftype', propname='ftype', displayname='File Type')
class CuckooDropped(CuckooEntity):
    pass
    
class CuckooOpenFile(CuckooEntity):
    pass

class CuckooMalwareFilename(CuckooEntity):
    pass

@EntityField(name='hashtype', propname='hashtype', displayname='Hash Type')
class CuckooHash(CuckooEntity):
    pass

@EntityField(name='vtlink', propname='vtlink', displayname='VT Link')
class CuckooVT(CuckooEntity):
    pass

class CuckooYara(CuckooEntity):
    pass

class CuckooMalwareSample(CuckooEntity):
    pass

class CuckooMutex(CuckooEntity):
    pass

class CuckooProcess(CuckooEntity):
    pass

class FileDetails(CuckooEntity):
    pass

class SignatureAnalysis(CuckooEntity):
    pass

class NetworkAnalysis(CuckooEntity):
    pass

class StaticAnalysis(CuckooEntity):
    pass

class DroppedFiles(CuckooEntity):
    pass

class BehaviorAnalysis(CuckooEntity):
    pass

class Processes(CuckooEntity):
    pass