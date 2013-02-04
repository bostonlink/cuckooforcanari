#!/usr/bin/env python

from canari.framework import configure
from canari.maltego.entities import Phrase
from common.entities import StaticAnalysis, CuckooTaskID, CuckooMalwareFilename
from common.cuckooapi import report
from common.cuckooparse import static_results

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
	label='To PE Sections [Cuckoo Sandbox]',
	description='Returns PE sections of the malware sample.',
	uuids=[ 'cuckooforcanari.v2.IDToCuckooPESec_Cuckoo',
			'cuckooforcanari.v2.FileToCuckooPESec_Cuckoo',
			'cuckooforcanari.v2.SectionToCuckooPESec_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ),
		( 'Cuckoo Sandbox', CuckooMalwareFilename ),
		( 'Cuckoo Sandbox', StaticAnalysis ) ],
	debug=False
)

def dotransform(request, response):

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value

	secs = static_results(report(task))['pe_sections']
	for d in secs:
		response += Phrase(d['name'].decode('ascii'))

	return response