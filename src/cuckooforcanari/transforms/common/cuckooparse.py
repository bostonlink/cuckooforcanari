#!/usr/bin/env python

# Cuckoo report parser python module for maltego transforms
# Author: David Bressler (@bostonlink)

# Returns dic of analysis information
def analysis_info(report):
	return report['info']

# Returns list of yara signatures
def yara_sigs(report):
	return report['yara']

# Returns list of cuckoo signatures
def cuckoo_sigs(report):
	return report['signatures']

# Returns dic of VT results
def vt_results(report):
	return report['virustotal']

# Returns dic of networking results
def network(report):
	return report['network']

# Returns dic of static analysis results
def static_results(report):
	return report['static']

# Returns list of dropped files
def dropped_files(report):
	return report['dropped']

# Returns dic of behavior results
def behavior(report):
	return report['behavior']

# Returns dic of debug logs for analysis
def debug_logs(report):
	return report['debug']

# Returns list of strings from sample
def strings(report):
	return report['strings']

# Returns dic of target file results
def target_info(report):
	return report['target']