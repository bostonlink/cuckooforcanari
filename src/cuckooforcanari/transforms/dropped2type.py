#!/usr/bin/env python

from canari.framework import configure
from canari.maltego.entities import Phrase
from common.entities import CuckooDropped
from common.cuckooapi import report
from common.cuckooparse import dropped_files

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
    label='To Dropped File Type [Cuckoo Sandbox]',
    description='Returns dropped file types during the Cuckoo file analysis.',
    uuids=[ 'cuckooforcanari.v2.IDToDroppedType_Cuckoo' ],
    inputs=[ ( 'Cuckoo Sandbox', CuckooDropped ) ],
    remote=False,
    debug=False
)
def dotransform(request, response, config):
    fname = request.value

    if 'taskid' in request.fields:
        task = request.fields['taskid']
    else:
        task = request.value

    dropped = dropped_files(report(task))
    for d in dropped:
        if d['name'] == fname:
            response += Phrase(d['type'].decode('ascii'))

    return response
