#!/usr/bin/env python

from canari.framework import configure
from common.entities import CuckooProcess, Processes, CuckooTaskID, CuckooMalwareFilename
from common.cuckooapi import report
from common.cuckooparse import behavior

__author__ = 'bostonlink'
__copyright__ = 'Copyright 2013, Cuckooforcanari Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'bostonlink'
__email__ = 'bostonlink@pentest-labs.org'
__status__ = 'Development'

__all__ = [
	'dotransform'
]

@configure(
	label='To Processes [Cuckoo Sandbox]',
	description='Returns processes created during the Cuckoo analysis.',
	uuids=[ 'cuckooforcanari.v2.IDToCuckooProcess_Cuckoo',
			'cuckooforcanari.v2.FileToCuckooProcess_Cuckoo',
			'cuckooforcanari.v2.SectionToCuckooProcess_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ),
		( 'Cuckoo Sandbox', CuckooMalwareFilename ),
		( 'Cuckoo Sandbox', Processes ) ],
	debug=False
)

def dotransform(request, response):

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value

	processes = behavior(report(task))['processes']
	for d in processes:
		response += CuckooProcess(
				d['process_name'].decode('ascii'),
				taskid = task )

	return response