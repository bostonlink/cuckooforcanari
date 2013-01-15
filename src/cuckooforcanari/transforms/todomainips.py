#!/usr/bin/env python

from canari.framework import configure
from canari.maltego.entities import IPv4Address, Domain
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
	label='To Domain IP [Cuckoo Sandbox]',
	description='Returns domain resolved IP address at the time of the Cuckoo file analysis.',
	uuids=[ 'cuckooforcanari.v2.IDToDomainIP_Cuckoo', 'cuckooforcanari.v2.FileToDomainIP_Cuckoo', 'cuckooforcanari.v2.DomainToDomainIP_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ), ( 'Cuckoo Sandbox', CuckooMalwareFilename ), ( 'Cuckoo Sandbox', Domain) ],
	debug=False
)

def dotransform(request, response):

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value

	netw = network(report(task))
	for d in netw['domains']:
			response += IPv4Address(
				d['ip'].decode('ascii'),
				taskid = task
			)

	return response