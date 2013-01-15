#!/usr/bin/env python

from canari.framework import configure
from common.entities import CuckooDropped, CuckooHash
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
	'dotransform'
]

@configure(
	label='To Dropped SHA1 [Cuckoo Sandbox]',
	description='Returns dropped file SHA1 hash',
	uuids=[ 'cuckooforcanari.v2.ToDroppedSHA1_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox', CuckooDropped ) ],
	debug=False
)

def dotransform(request, response):
	fname = request.value

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value

	dropped = dropped_files(report(task))
	for d in dropped:
		if d['name'] == fname:
			response += CuckooHash(d['sha1'].decode('ascii'))

	return response