## Importing packages
import argparse

## Import required functions from utils
from utils import *

## Main function
def main(args):

	executeSplit(args.srcDir, args.rTrain, args.classes, args.seed)

	print('\nExited main.py.')

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Reading info for main.')

	# Arguments to execute test/train split.
	parser.add_argument('--srcDir', action='store', nargs='?', type=str, default='input/example/*.tif', help='Source frames.')
	parser.add_argument('--rTrain', action='store', nargs='?', type=float, default=0.8, help='Ratio of train images.')
	parser.add_argument('--classes', action='store', nargs='+', default=['d'], help='Classes to store.')
	parser.add_argument('--seed', action='store', nargs='?', type=int, default=100, help='Seed for random split.')
	# Example:
	# python main.py --srcDir input/example/*.tif --rTrain 0.8 --classes d --seed 100

	# Parse arguments
	args = parser.parse_args()

	# Call main
	main(args)