#!/usr/bin/env python

from canari.framework import configure
from common.entities import CuckooHash, CuckooMalwareFilename, CuckooTaskID
from common.cuckooapi import report
from common.cuckooparse import target_info

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
	label='To SHA1 [Cuckoo Sandbox]',
	description='Returns filename of the initial file analyzed.',
	uuids=[ 'cuckooforcanari.v2.IDToSHA1_Cuckoo', 'cuckooforcanari.v2.FileToSHA1_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ), ( 'Cuckoo Sandbox', CuckooMalwareFilename )  ],
	debug=True
)

def dotransform(request, response):

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value

	# TODO Figure out the link, notes, and bookmark entity props
	target = target_info(report(task))['file']
	
	response += CuckooHash(
				target['sha1'].decode('ascii'),
				taskid = task
			)

	return response