#!/usr/bin/env python

import os.path
from time import sleep
from canari.framework import configure
from canari.config import config
from common.entities import CuckooMalwareSample, CuckooTaskID
from common.cuckooapi import submit_file, task_view

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
    description='Submits a File to Cuckoo and returns the analysis task id after analysis is complete.',
    uuids=[ 'cuckooforcanari.v2.SubmitFile_Cuckoo' ],
    inputs=[ ( 'Cuckoo Sandbox', CuckooMalwareSample ) ],
    debug=True
)

def dotransform(request, response):

	sample = os.path.join(config['cuckoo/malware_dir'], request.value)
	task = submit_file(sample)['task_id']
	status = task_view(task)['task']['status']

	# Check status of task loop
	while status == 'pending' or status == 'processing':
		sleep(20)
		status = task_view(task)['task']['status']

	response += CuckooTaskID(
                task,
                status = status,
                filename = sample
	    )

	return response