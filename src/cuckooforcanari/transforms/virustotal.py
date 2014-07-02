#!/usr/bin/env python

from canari.framework import configure
from common.entities import CuckooVT, SignatureAnalysis, CuckooTaskID, CuckooMalwareFilename
from common.cuckooapi import report
from common.cuckooparse import vt_results

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
    label='To VirusTotal Results [Cuckoo Sandbox]',
    description='Returns Yara signature names associated with the Cuckoo analysis task id.',
    uuids=[ 'cuckooforcanari.v2.IDToVTresults_Cuckoo', 
            'cuckooforcanari.v2.FileToVTResults_Cuckoo',
            'cuckooforcanari.v2.SectionToVTResults_Cuckoo' ],
    inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ),
        ( 'Cuckoo Sandbox', CuckooMalwareFilename ),
        ( 'Cuckoo Sandbox', SignatureAnalysis )],
    remote=False,
    debug=False
)
def dotransform(request, response, config):

    if 'taskid' in request.fields:
        task = request.fields['taskid']
    else:
        task = request.value

    vt = vt_results(report(task))
    if vt['response_code'] == 1:
        for k, v in vt['scans'].iteritems():
            if None != v['result']:
                value = k + ' - ' + v['result']
                response += CuckooVT(
                    value.decode('ascii'),
                    taskid=task,
                    vtlink=vt['permalink']
                )
    else:
        pass

    return response
