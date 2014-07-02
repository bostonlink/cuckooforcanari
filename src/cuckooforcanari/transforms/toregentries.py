#!/usr/bin/env python

from canari.framework import configure
from canari.maltego.entities import Phrase
from common.entities import BehaviorAnalysis, CuckooTaskID, CuckooMalwareFilename
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
    label='To Registry Keys [Cuckoo Sandbox]',
    description='Returns registry keys created during the Cuckoo analysis.',
    uuids=[ 'cuckooforcanari.v2.IDToCuckooRegKeys_Cuckoo',
            'cuckooforcanari.v2.FileToCuckooRegKeys_Cuckoo',
            'cuckooforcanari.v2.SectionToCuckooRegKeys_Cuckoo' ],
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

    reg = behavior(report(task))['summary']['keys']
    for d in reg:
        response += Phrase(d.decode('ascii'))

    return response
