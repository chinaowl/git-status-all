import sys
import os
import subprocess

root_dir = './'

if len(sys.argv) > 1:
	root_dir = sys.argv[1]

if not root_dir.endswith('/'):
	root_dir += '/'

subdirs = os.listdir(root_dir)

def not_hidden(item):
	return not item.startswith('.')

subdirs = filter(not_hidden, subdirs)

for subdir in subdirs:
	os.chdir(root_dir + subdir)

	print 'Checking ' + os.getcwd()

	if '.git' in os.listdir('./'):
		status = subprocess.check_output(['git', 'status'])
		if 'Your branch is ahead' in status:
			print 'You have local commits to push'
		if 'Changes not staged for commit' in status:
			print 'You have changes to commit'
		if 'nothing to commit, working directory clean' in status:
			print 'You have nothing to commit'
		if 'nothing added to commit but untracked files present' in status:
			print 'You have untracked files'
	else:
		print 'Not a git repository'

	print
