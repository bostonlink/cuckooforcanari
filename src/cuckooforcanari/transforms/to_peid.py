#!/usr/bin/env python

from canari.framework import configure
from canari.maltego.entities import Phrase
from common.entities import StaticAnalysis, CuckooTaskID, CuckooMalwareFilename
from common.cuckooapi import report
from common.cuckooparse import static_results

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
    label='To PEID Signature [Cuckoo Sandbox]',
    description='Returns PEID signature of the malware sample.',
    uuids=[ 'cuckooforcanari.v2.IDToCuckooPEIDSig_Cuckoo',
            'cuckooforcanari.v2.FileToCuckooPEIDSig_Cuckoo',
            'cuckooforcanari.v2.SectionToCuckooPEIDSig_Cuckoo' ],
    inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ),
        ( 'Cuckoo Sandbox', CuckooMalwareFilename ),
        ( 'Cuckoo Sandbox', StaticAnalysis ) ],
    remote=False,
    debug=False
)
def dotransform(request, response, config):

    if 'taskid' in request.fields:
        task = request.fields['taskid']
    else:
        task = request.value

    secs = static_results(report(task))['peid_signatures']
    if secs is None:
        pass
    else:
        for i in secs:
            response += Phrase(i)

    return response
