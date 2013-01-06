#!/usr/bin/env python

# Cuckoo API python module for maltego transforms
# Author: David Bressler (@bostonlink)

# Cuckoo API Documentation http://docs.cuckoosandbox.org/en/latest/usage/api/

import requests
from canari.config import config
from canari.maltego.message import MaltegoException

# Submit file for analysis
def submit_file(sample):
	url = 'http://%s:%s/tasks/create/file' % (config['cuckoo/host'], config['cuckoo/port'])
	samples = {'file': open(sample, 'rb')}
	try:
		r = requests.post(url, files=samples)
		return r.json()
	except Exception as e:
		raise MaltegoException("The Transform has returned: %s" % e)

# Submit URL for analysis
def submit_url(analysis_url):
	url = 'http://%s:%s/tasks/create/url' % (config['cuckoo/host'], config['cuckoo/port'])
	if analysis_url.startswith('http://') or analysis_url.startswith('https://'):
		data = {'url': analysis_url}
	else:
		analysis_url = 'http://' + analysis_url
		data = {'url': analysis_url}

	try:
		r = requests.post(url, data=data)
		return r.json()
	except Exception as e:
		raise MaltegoException("The Transform has returned: %s" % e)

# Return task list
def task_list():
	url = 'http://%s:%s/tasks/list' % (config['cuckoo/host'], config['cuckoo/port'])
	try:
		r = requests.get(url)
		return r.json()
	except Exception as e:
		raise MaltegoException("The Transform has returned: %s" % e)

# Returns task status
def task_view(task_id):
	url = 'http://%s:%s/tasks/view/%s' % (config['cuckoo/host'], config['cuckoo/port'], task_id)
	try:
		r = requests.get(url)
		return r.json()
	except Exception as e:
		raise MaltegoException("The Transform has returned: %s" % e)

# Returns full report
def report(task_id):
	url = 'http://%s:%s/tasks/report/%s' % (config['cuckoo/host'], config['cuckoo/port'], task_id)
	try:
		r = requests.get(url)
		return r.json()
	except Exception as e:
		raise MaltegoException("The Transform has returned: %s" % e)

# Returns file details from a task id
def file_search_id(task_id):
	url = 'http://%s:%s/files/view/id/%s' % (config['cuckoo/host'], config['cuckoo/port'], task_id)
	try:
		r = requests.get(url)
		return r.json()
	except Exception as e:
		raise MaltegoException("The Transform has returned: %s" % e)

# Returns file details from a sha256 hash
def file_search_sha256(sha256):
	url = 'http://%s:%s/files/view/sha256/%s' % (config['cuckoo/host'], config['cuckoo/port'], sha256)
	try:
		r = requests.get(url)
		return r.json()
	except Exception as e:
		raise MaltegoException("The Transform has returned: %s" % e)

# Returns file details from a md5 hash
def file_search_md5(md5):
	url = 'http://%s:%s/files/view/md5/%s' % (config['cuckoo/host'], config['cuckoo/port'], md5)
	try:
		r = requests.get(url)
		return r.json()
	except Exception as e:
		raise MaltegoException("The Transform has returned: %s" % e)