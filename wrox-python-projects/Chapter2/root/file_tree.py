import os, re
import os.path as path

def find_files(pattern, base='.'):
	""" Finds files under base based on pattern...
	walks the fle system starting at base and
	returns a list of filenames matching pattern"""

	regex = re.compile(pattern)
	matches = []
	for root, dirs, files in os.walk(base):
		for f in files:
			if regex.match(f):
				matches.append(path.join(root,f))
	return matches
