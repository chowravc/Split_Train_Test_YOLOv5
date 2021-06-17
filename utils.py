## Importing packages
import numpy as np
import shutil
import cv2
import glob
import os
import random

## Create test/train split for YOLOv5
def executeSplit(sourceDir, ratio, classes, rSeed):

	print('\nChecking frames: ' + sourceDir)

	# Frames paths
	fPath = glob.glob(sourceDir)

	# If no input found
	if len(fPath) == 0:

		print('\nInput not found.')

	# If input is found
	else:

		print('Found ' + str(len(fPath)) + ' input frames.')

		# If output directory does not exist
		if len(glob.glob('output/')) == 0:

			os.mkdir('./output/')

		outDir = './output/' + sourceDir.split('/')[-2] + '/'

		# If output does exist, clear it
		if len(glob.glob(outDir)) > 0:

			print('Clearing output dir.\n')

			shutil.rmtree(outDir)

		# Make output directory again
		os.mkdir(outDir)

		dataDir = outDir + sourceDir.split('/')[-2] + '/'

		# Creating data director
		os.mkdir(dataDir)

		# Making train/test directories
		os.mkdir(dataDir + 'labels/')
		os.mkdir(dataDir + 'images/')

		os.mkdir(dataDir + 'labels/test/')
		os.mkdir(dataDir + 'images/test/')

		os.mkdir(dataDir + 'labels/train/')
		os.mkdir(dataDir + 'images/train/')

		# Shuffling paths
		random.Random(rSeed).shuffle(fPath)

		# Finding number of train images
		nTrain = len(fPath) - int(len(fPath)*0.2)

		print('Performing split.\n')
		# For every file
		for i, fileSrc in enumerate(fPath):

			# Displaying progress
			if i%100 == 0:

				print(str(100*i/len(fPath))[:4] + '%')

			# If it should go to train
			if i < nTrain:

				intermediary = dataDir + 'images/train/'

			# If it should go to test
			else:

				intermediary = dataDir + 'images/test/'

			# Figuring out filename
			fileName = fileSrc.split('\\')[-1]

			# Figuring out destination
			fileDest = intermediary + fileName

			# Copying over the file
			shutil.copyfile(fileSrc, fileDest)

		# Reading classfile template
		template = open('template.yaml', 'r')

		# Data inside yaml
		tempTxt = template.read()

		## Replacing template phrases

		# Replacing directory to test/train with name of set
		tempTxt = tempTxt.replace('template', sourceDir.split('/')[-2])

		# Replacing number of classes with number of classes
		tempTxt = tempTxt.replace('numberClasses', str(len(classes)))

		# Replacing 'list' phrase with list of classes
		tempTxt = tempTxt.replace('classList', repr(classes))

		# Replacing number of test/train images (purely for reference)
		tempTxt = tempTxt.replace('numberOfTrain', str(nTrain))
		tempTxt = tempTxt.replace('numberOfTest', str(len(fPath) - nTrain))

		# yaml file name
		yamlOut = outDir + sourceDir.split('/')[-2] + '.yaml'

		# Saving yaml file
		with open(yamlOut, 'w') as yFile:
			yFile.write(tempTxt)

		print('\nFinished split.')