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
	'dotransform',
	'onterminate'
]

@configure(
	label='To Dropped SHA256 [Cuckoo Sandbox]',
	description='Returns dropped file SHA256 hash',
	uuids=[ 'cuckooforcanari.v2.ToDroppedSHA256_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox', CuckooDropped ) ],
	debug=True
)

def dotransform(request, response):
	fname = request.value

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value

	# TODO Figure out the link, notes, and bookmark entity props
	dropped = dropped_files(report(task))
	for d in dropped:
		if d['name'] == fname:
			response += CuckooHash(d['sha256'].decode('ascii'))

	return response