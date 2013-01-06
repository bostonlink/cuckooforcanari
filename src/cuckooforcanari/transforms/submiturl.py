#!/usr/bin/env python

from time import sleep
from canari.framework import configure
from canari.maltego.entities import URL
from common.entities import CuckooTaskID
from common.cuckooapi import submit_url, task_view

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
    label='Submit File for Analysis [Cuckoo Sandbox]',
    description='Submits a file sample to Cuckoo and returns the analysis task id after analysis is complete.',
    uuids=[ 'cuckooforcanari.v2.SubmitURL_Cuckoo' ],
    inputs=[ ( 'Cuckoo Sandbox', URL ) ],
    debug=True
)

def dotransform(request, response):

	url = request.value
	task = submit_url(url)['task_id']
	status = task_view(task)['task']['status']

	# Check status of task loop
	while status == 'pending' or status == 'processing':
		sleep(20)
		status = task_view(task)['task']['status']

	response += CuckooTaskID(
                task,
                status = status,
                url = url
	    )

	return response