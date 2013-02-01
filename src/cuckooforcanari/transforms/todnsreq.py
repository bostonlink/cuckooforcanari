#!/usr/bin/env python

from canari.framework import configure
from canari.maltego.entities import NSRecord
from common.entities import CuckooTaskID, CuckooMalwareFilename
from common.cuckooapi import report
from common.cuckooparse import network

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
	label='To DNS Request [Cuckoo Sandbox]',
	description='Returns DNS requests made during the Cuckoo file analysis.',
	uuids=[ 'cuckooforcanari.v2.IDToDNSReq_Cuckoo', 'cuckooforcanari.v2.FileToDNSReq_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ), ( 'Cuckoo Sandbox', CuckooMalwareFilename ) ],
	debug=False
)

def dotransform(request, response):

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value

	netw = network(report(task))
	dns_lst = []
	for d in netw['dns']:
		if d['request'] not in dns_lst:
			response += NSRecord(
				d['request'].decode('ascii'),
				taskid = task
			)
			dns_lst.append(d['request'])

	return response