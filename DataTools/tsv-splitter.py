import argparse, glob, os, logging
from sys import stdout

# Disclaimer: This script was made to be used in a Linux terminal
# 
# Purpose: TSV files are annoying, and so are suitably large ones
#          I wrote this script to automate splitting them into smaller file sizes
#
# Usage:
#
#   The script makes a backup of the .tsv file you give it,
#   It creates a folder with the same name as the file name
#   It generates smaller TSV files and puts them in the new folder
#
# - Download or copy raw and paste into a .py file
#
# - The script can be called with: python file.py [tsv_file] [prefix] [line-count]
#
#   + [tsv_file]   :	the file you wish to break into smaller files
#   + [prefix]	   :	the name prefix to give the new, smaller files
#   + [line-count] :	the maximum number of lines you want in the new, smaller files
#

def make_backup(working, parent, file):

	# create a backup directory
	backup_dir = working + 'originals/'
	try:

		os.mkdir(backup_dir)
		logger.info('Backup directory: \"./originals/\" created successfully.')

	except FileExistsError:

		# Remind the user of the backup directory
		logger.warning('Backup directory: \"./originals/\" already exists.')
		pass

	backup_path = backup_dir + '/' + file + '.bak'
	backup = 'cp ' + parent + ' ' + backup_path
	os.system(backup)


def make_tsvs(parent, prefix, lines):

	# make a directory matching the parent file name
	parent_dir = parent[:-4] + '/'
	try:

		os.mkdir(parent_dir)
		logger.info('Destination directory: \"' + parent_dir + '\" created successfully.')
		
	except FileExistsError:

		# inform the user that this directory already exists
		# (they might have a big mess to look through)
		logger.warning('Destination directory: \"' + parent_dir + '\" already exists.')
		pass

	# split the parent tsv into smaller tsv files
	cmd = f'split -l {lines} {parent} {prefix}'
	os.system(cmd)

	# This block achieves two things:
	# 1) Find all files containing the prefix (they have no extension)
	# 2) Rename each file by performing a file move (put into a new folder)
	files = []
	pattern = './' + prefix + '*'
	for file in glob.glob(pattern):
		if prefix in file:
			rename = parent_dir + file + '.tsv'
			files.append(rename)
			os.system('mv ' + file + ' ' + rename)

	return parent_dir, len(files)


# current workng directory
working = os.getcwd() + '/'

# adding a logger so we can warn in stdout if a directory we try to make already exists
logger = logging.getLogger()
streamHandler = logging.StreamHandler(stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# arg parsing to make sure we get a file and a re-name prefix
parser = argparse.ArgumentParser(description='Split a large TSV into smaller ones of 10000 lines or less.')
parser.add_argument('infile', metavar='[file]', type=str, help='The file to be processed.')
parser.add_argument('prefix', metavar='[prefix]', type=str, help='Prefix for new files.')
parser.add_argument('lines', metavar='[line-count]', type=int, help='# of lines per new file.')
args = parser.parse_args()

# path of the file passed in
path = working + args.infile

if os.path.exists(args.infile):

  # file is valid, make a backup, and split the file into smaller ones
	make_backup(working, path, args.infile)
	parent, file_count = make_tsvs(path, args.prefix, args.lines)

	# inform the user how many files were processed and where to find them
	msg = f'{file_count} TSV files were generated.\n' \
	       'Visit the \"{parent}\" folder to access them.'
	logger.info(msg)

	exit()
else:
	logger.error('File does not exist.')
	exit()
