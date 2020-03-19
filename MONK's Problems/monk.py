# P&S Assignment 3
# Name: ADWIT SINGH KOCHAR
# Roll Number: 2018276
# Section: A
# Group: 8

"""
	Calculates accuracy for the 3 MONK's Problems Data Sets. It first calculates them individually and then
	calculates for the combined dataset.
"""
import csv

files = ['monks-1', 'monks-2', 'monks-3', 'monks-combined']
flag = True

for name in files:
	
	positive = [{'1':0, '2':0, '3':0, '4':0} for x in range(8)]						# Calculated Constants
	negative = [{'1':0, '2':0, '3':0, '4':0} for x in range(8)]
	countTrain = 0
	countTest = 0
	rightPrediction = 0
	positiveCount = 0
	negativeCount = 0

	with open(name + '.train') as csv_file:											# TRAINING
		csv_reader = csv.reader(csv_file, delimiter=' ')

		for row in csv_reader:
			countTrain += 1

			if(row[1] == '1'):
				positiveCount += 1
				for i in range(2,8):
					positive[i][row[i]] +=1
			else:
				negativeCount += 1
				for i in range(2,8):
					negative[i][row[i]] +=1

	with open(name + '.test') as csv_file:											# TESTING
		csv_reader = csv.reader(csv_file, delimiter=' ')

		for row in csv_reader:
			countTest+=1

			probPositive = positiveCount/countTrain
			probNegative = negativeCount/countTrain

			for i in range(2,8):
				probPositive *= (positive[i][row[i]])/positiveCount
				probNegative *= (negative[i][row[i]])/negativeCount

			if(probPositive > probNegative):
				if(row[1] == '1'):
					rightPrediction+=1
			elif(probNegative > probPositive):
				if(row[1] == '0'):
					rightPrediction+=1 

	accuracy = round(rightPrediction/countTest, 7) * 100
	
	if(flag):
		with open('result','w') as output:
		 	output.write(str(accuracy) + '\n')
		flag = False
	else:
		with open('result','a') as output:
		 	output.write(str(accuracy) + '\n')
