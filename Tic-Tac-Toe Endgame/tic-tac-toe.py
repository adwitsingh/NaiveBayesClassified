# P&S Assignment 3
# Name: ADWIT SINGH KOCHAR
# Roll Number: 2018276
# Section: A
# Group: 8

"""
	Calculates accuracy for Tic-Tac-Toe Endgame Dataset
"""
import csv

positive = [{'x':0,'o':0,'b':0} for x in range(9)]								# Calculated Constants
negative = [{'x':0,'o':0,'b':0} for x in range(9)]
count = 0
rightPrediction = 0
positiveCount = 0
negativeCount = 0

with open('tic-tac-toe.data') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	for row in csv_reader:														# TRAINING
		count += 1
		if(row[9] == 'positive'):
			positiveCount += 1
			for i in range(9):
				positive[i][row[i]] +=1
		else:
			negativeCount += 1
			for i in range(9):
				negative[i][row[i]] +=1

	csv_file.seek(0)
	

	for row in csv_reader:														# TESTING
		tempCount = count - 1
		tempPositiveCount = positiveCount if row[9] != 'positive' else positiveCount-1
		tempNegativeCount = negativeCount if row[9] != 'negative' else negativeCount-1

		probPositive = tempPositiveCount/tempCount
		probNegative = tempNegativeCount/tempCount

		for i in range(9):
			if(row[9] == 'positive'):
				probPositive *= (positive[i][row[i]]-1)/tempPositiveCount
				probNegative *= (negative[i][row[i]])/tempNegativeCount
			else:
				probPositive *= (positive[i][row[i]])/tempPositiveCount
				probNegative *= (negative[i][row[i]]-1)/tempNegativeCount

		if(probPositive > probNegative):
			if(row[9] == 'positive'):
				rightPrediction+=1
		elif(probNegative > probPositive):
			if(row[9] == 'negative'):
				rightPrediction+=1 

accuracy = round(rightPrediction/count, 7) * 100

with open('result','w') as output:
	output.write(str(accuracy))