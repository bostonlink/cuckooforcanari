#!/usr/bin/env python

from canari.framework import configure
from common.entities import CuckooSig, CuckooTaskID, CuckooMalwareFilename
from common.cuckooapi import report
from common.cuckooparse import cuckoo_sigs

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
	label='To Cuckoo Community Signatures [Cuckoo Sandbox]',
	description='Returns Cuckoo signature names hit during the Cuckoo file analysis.',
	uuids=[ 'cuckooforcanari.v2.IDToCuckooSigs_Cuckoo', 'cuckooforcanari.v2.FileToCuckooSigs_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ), ( 'Cuckoo Sandbox', CuckooMalwareFilename ) ],
	debug=False
)

def dotransform(request, response):

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value

	csigz = cuckoo_sigs(report(task))
	for d in csigz:
		response += CuckooSig(
				d['description'].decode('ascii'),
				taskid = task,
		)

	return response