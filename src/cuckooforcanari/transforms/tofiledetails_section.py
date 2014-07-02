#!/usr/bin/env python

from canari.framework import configure
from common.entities import FileDetails, CuckooTaskID, CuckooMalwareFilename

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
    label='To File Details Section [Cuckoo Sandbox]',
    description='Returns file details section entity, to separate analysis sections.',
    uuids=[ 'cuckooforcanari.v2.IDToFileDetailsSection_Cuckoo', 'cuckooforcanari.v2.FileToFileDetailsSection_Cuckoo' ],
    inputs=[ ( 'Cuckoo Sandbox Analysis Sections', CuckooTaskID ), ( 'Cuckoo Sandbox Analysis Sections', CuckooMalwareFilename ) ],
    debug=False
)
def dotransform(request, response):

    if 'taskid' in request.fields:
        task = request.fields['taskid']
    else:
        task = request.value
    response += FileDetails('File Details', taskid = task)
    return response
