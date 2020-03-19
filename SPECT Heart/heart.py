# P&S Assignment 3
# Name: ADWIT SINGH KOCHAR
# Roll Number: 2018276
# Section: A
# Group: 8

"""
	Calculates accuracy for SPECT Heart Dataset
"""
import csv

positive = [{'0':0, '1':0} for x in range(23)]									# Calculated Constants
negative = [{'0':0, '1':0} for x in range(23)]
countTrain = 0
countTest = 0
rightPrediction = 0
positiveCount = 0
negativeCount = 0

with open('SPECT.train') as csv_file:											# TRAINING
	csv_reader = csv.reader(csv_file, delimiter=',')

	for row in csv_reader:
		countTrain += 1

		if(row[0] == '1'):
			positiveCount += 1
			for i in range(1,23):
				positive[i][row[i]] +=1
		else:
			negativeCount += 1
			for i in range(1,23):
				negative[i][row[i]] +=1

with open('SPECT.test') as csv_file:											# TESTING
	csv_reader = csv.reader(csv_file, delimiter=',')

	for row in csv_reader:
		countTest+=1

		probPositive = positiveCount/countTrain
		probNegative = negativeCount/countTrain

		for i in range(1,23):
			probPositive *= (positive[i][row[i]])/positiveCount
			probNegative *= (negative[i][row[i]])/negativeCount

		if(probPositive > probNegative):
			if(row[0] == '1'):
				rightPrediction+=1
		elif(probNegative > probPositive):
			if(row[0] == '0'):
				rightPrediction+=1 

accuracy = round(rightPrediction/countTest, 7) * 100

with open('result','w') as output:
	output.write(str(accuracy))
