#!/usr/bin/env python

from canari.framework import configure
from common.entities import CuckooMutex, BehaviorAnalysis, CuckooTaskID, CuckooMalwareFilename
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
    label='To Mutexes [Cuckoo Sandbox]',
    description='Returns mutexes created during the Cuckoo analysis.',
    uuids=[ 'cuckooforcanari.v2.IDToCuckooMutex_Cuckoo',
            'cuckooforcanari.v2.FileToCuckooMutex_Cuckoo',
            'cuckooforcanari.v2.SectionToCuckooMutex_Cuckoo' ],
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

    mutexes = behavior(report(task))['summary']['mutexes']
    for d in mutexes:
        response += CuckooMutex(
                d.decode('ascii'),
                taskid=task)

    return response
