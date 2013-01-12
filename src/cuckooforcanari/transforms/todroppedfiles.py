#!/usr/bin/env python

from canari.framework import configure
from common.entities import CuckooDropped, CuckooTaskID, CuckooMalwareFilename
from common.cuckooapi import report
from common.cuckooparse import dropped_files

__author__ = 'bostonlink'
__copyright__ = 'Copyright 2013, Cuckooforcanari Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'bostonlink'
__email__ = 'bostonlink@pentest-labs.org'
__status__ = 'Development'

__all__ = [
	'dotransform',
	'onterminate'
]

@configure(
	label='To Dropped Files [Cuckoo Sandbox]',
	description='Returns dropped files during the Cuckoo file analysis.',
	uuids=[ 'cuckooforcanari.v2.IDToDropped_Cuckoo', 'cuckooforcanari.v2.FileToDropped_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ), ( 'Cuckoo Sandbox', CuckooMalwareFilename ) ],
	debug=True
)

def dotransform(request, response):

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value

	dropped = dropped_files(report(task))
	for d in dropped:
			response += CuckooDropped(
				d['name'].decode('ascii'),
				taskid = task,
				ftype = d['type']
			)

	return response