#!/usr/bin/env python

from canari.framework import configure
from common.entities import DroppedFiles, CuckooTaskID, CuckooMalwareFilename

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
    label='To Dropped Files Section [Cuckoo Sandbox]',
    description='Returns dropped files section entity, used to separate analysis sections.',
    uuids=[ 'cuckooforcanari.v2.IDToDroppedFilessection_Cuckoo', 'cuckooforcanari.v2.FileToDroppedFilesSection_Cuckoo' ],
    inputs=[ ( 'Cuckoo Sandbox Analysis Sections', CuckooTaskID ), ( 'Cuckoo Sandbox Analysis Sections', CuckooMalwareFilename ) ],
    remote=False,
    debug=False
)
def dotransform(request, response, config):

    if 'taskid' in request.fields:
        task = request.fields['taskid']
    else:
        task = request.value
    response += DroppedFiles('Dropped Files', taskid=task)
    return response
