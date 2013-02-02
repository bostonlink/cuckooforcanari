#!/usr/bin/env python

from canari.framework import configure
from common.entities import NetworkAnalysis, CuckooTaskID, CuckooMalwareFilename

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
	label='To Network Analysis Section [Cuckoo Sandbox]',
	description='Returns network analysis section entity, used to separate analysis sections.',
	uuids=[ 'cuckooforcanari.v2.IDToNetAnalysisSection_Cuckoo', 'cuckooforcanari.v2.FileToNetAnalysisSection_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox Analysis Sections', CuckooTaskID ), ( 'Cuckoo Sandbox Analysis Sections', CuckooMalwareFilename ) ],
	debug=False
)

def dotransform(request, response):

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value
	response += NetworkAnalysis('Network Analysis', taskid = task)
	return response