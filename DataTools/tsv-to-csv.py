import argparse, click, glob, logging, os, time
import pandas as pd
from sys import stdout



# Disclaimer: This script was made to be used in a Linux environment (terminal)
# 
# Purpose:
#   Converts TSV files to CSV format in bulk
#   I wrote it to be used by itself or with my other
#	script for splitting TSV files into smaller ones
#
# Usage:
#
#   Converts .tsv files to .csv in bulk,
#	when a .csv made, its .tsv counterpart is deleted
#   
#	Note: Runs kind of slow. Pandas has to read in chunks
#		  just in case a line is large in size to prevent
#		  running low on memory. If you know it won't be a
#		  problem then just increase the chunk size below.
# 
# - Download or copy raw and paste into a .py file
#
# - The script can be called with: python file.py [directory]
#
#   + [directiory]	: optional,
#			  if you want to specify a directory other than the current one
#
#


def to_digital(interval):
	'''Convert a time elapsed in seconds to a digital clock'''
	minutes, seconds = divmod(interval, 60)
	hours, minutes = divmod(minutes, 60)
	digital = str(hours) + ':' + str(minutes) + ':' + str(seconds)

	return digital


def make_csv(tsv):
	'''Convert a tsv file to csv using pandas'''
	ext = 'csv'
	csv_name = tsv[:-3] + ext

	# create the csv file to put our converted data into
	with open(csv_name, 'w'):
		pass


	# chunksize can be increased if the lines in your TSV aren't huge
	for chunk in pd.read_table(tsv, sep='\t', chunksize=1):
		chunk.to_csv(csv_name, mode='a', index=False, header=False)

	return csv_name


# current working directory
working = os.getcwd() + '/'


# adding a logger so we can warn in stdout if a directory we try to make already exists
logger = logging.getLogger()
streamHandler = logging.StreamHandler(stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


# handle arguments passed in
desc = f'Given a directory, convert all TSV files in the directory to CSV format.'
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('dir', metavar='directory', nargs='?', default='.', type=str, help='The directory containing the TSV files')
args = parser.parse_args()


# handle if provided directory doesn't exist
if args.dir != '.':
	if not os.path.isdir(args.dir):
		logger.error(f'Directory \"{args.dir}\" does not exist.')
		exit()


# change the current working directory to the one passed in (or default)
os.chdir(args.dir)
pattern = working + args.dir + '/*.tsv'


# get a list of files to process
files = []
for file in glob.glob(pattern):
	files.append(file)
file_count = str(len(files))


# A few things:
# 1) inform the user of what's happening
# 2) keep track of elapsed time
# 3) display a progress bar
# 4) make calls to our conversion function
# 5) remove tsv files after they're processed
#
logger.info('Converting: ' + file_count + ', files from tsv to csv ...')
start = time.perf_counter()
with click.progressbar(files) as bar:
	for file in bar:
		make_csv(file)
		os.system('rm ' + file)
end = time.perf_counter()


# compute time elapsed
interval = round(end - start)
elapsed = to_digital(interval)


# let the user know we're done once they get back with their coffee (or tea)
stats = 'Processed: ' + file_count + ', in: ' + elapsed
logger.info(stats)
logger.info('Done.')

