#!/usr/bin/env python

from canari.framework import configure
from common.entities import CuckooOpenFile, BehaviorAnalysis, CuckooTaskID, CuckooMalwareFilename
from common.cuckooapi import report
from common.cuckooparse import behavior

__author__ = 'bostonlink'
__copyright__ = 'Copyright 2014, Cuckooforcanari Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '1.1'
__maintainer__ = 'bostonlink'
__email__ = 'bostonlink@pentest-labs.org'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


@configure(
    label='To Files Opened [Cuckoo Sandbox]',
    description='Returns opened and created files during the Cuckoo analysis.',
    uuids=[ 'cuckooforcanari.v2.IDToCuckooFOpen_Cuckoo',
            'cuckooforcanari.v2.FileToCuckooFOpen_Cuckoo',
            'cuckooforcanari.v2.SectionToCuckooFOpen_Cuckoo' ],
    inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ),
        ( 'Cuckoo Sandbox', CuckooMalwareFilename ),
        ( 'Cuckoo Sandbox', BehaviorAnalysis ) ],
    debug=False
)
def dotransform(request, response):

    if 'taskid' in request.fields:
        task = request.fields['taskid']
    else:
        task = request.value

    files = behavior(report(task))['summary']['files']
    for d in files:
        response += CuckooOpenFile(d.decode('ascii'),
                                   taskid=task)

    return response
