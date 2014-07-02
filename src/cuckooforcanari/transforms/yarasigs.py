#!/usr/bin/env python

from canari.framework import configure
from common.entities import CuckooYara, SignatureAnalysis, CuckooTaskID, CuckooMalwareFilename
from common.cuckooapi import report
from common.cuckooparse import yara_sigs

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
    label='To Yara Signatures [Cuckoo Sandbox]',
    description='Returns Yara signature names associated with the Cuckoo analysis task id.',
    uuids=[ 'cuckooforcanari.v2.IDToYaraSigs_Cuckoo', 
            'cuckooforcanari.v2.FileToYaraSigs_Cuckoo',
            'cuckooforcanari.v2.SectionToYaraSigs_Cuckoo' ],
    inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ), 
        ( 'Cuckoo Sandbox', CuckooMalwareFilename ),
        ( 'Cuckoo Sandbox', SignatureAnalysis ) ],
    remote=False,
    debug=False
)
def dotransform(request, response, config):

    if 'taskid' in request.fields:
        task = request.fields['taskid']
    else:
        task = request.value

    ysigz = yara_sigs(report(task))
    for d in ysigz:
        for k, v in d.iteritems():
            if 'meta' in k:
                response += CuckooYara(
                    v['description'].decode('ascii'),
                    taskid=task,
                )

    return response
