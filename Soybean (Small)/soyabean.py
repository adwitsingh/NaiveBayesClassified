# P&S Assignment 3
# Name: ADWIT SINGH KOCHAR
# Roll Number: 2018276
# Section: A
# Group: 8

"""
	Calculates accuracy for SoyBean (Small) Dataset
"""
import csv
import operator

D1 = [dict() for x in range(35)]										# Calculated Constants
D2 = [dict() for x in range(35)]
D3 = [dict() for x in range(35)]
D4 = [dict() for x in range(35)]
count = 0
rightPrediction = 0
D1count = 0
D2count = 0
D3count = 0
D4count = 0

with open('soybean-small.data') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	for row in csv_reader:												# TRAINING
		count += 1

		exec(row[35] + "count += 1")
		for i in range(35):
			if(row[35] == 'D1'):
				if(row[i] in D1[i]):
					D1[i][row[i]] += 1
				else:
					D1[i][row[i]] = 1
			elif(row[35] == 'D2'):
				if(row[i] in D2[i]):
					D2[i][row[i]] += 1
				else:
					D2[i][row[i]] = 1
			elif(row[35] == 'D3'):
				if(row[i] in D3[i]):
					D3[i][row[i]] += 1
				else:
					D3[i][row[i]] = 1
			elif(row[35] == 'D4'):
				if(row[i] in D4[i]):
					D4[i][row[i]] += 1
				else:
					D4[i][row[i]] = 1

	csv_file.seek(0)

	for row in csv_reader:														# TESTING
		tempCount = count - 1
		tempD1Count = D1count if row[35] != 'D1' else D1count-1
		tempD2Count = D2count if row[35] != 'D2' else D2count-1
		tempD3Count = D3count if row[35] != 'D3' else D3count-1
		tempD4Count = D4count if row[35] != 'D4' else D4count-1

		probD1 = tempD1Count/tempCount
		probD2 = tempD2Count/tempCount
		probD3 = tempD3Count/tempCount
		probD4 = tempD4Count/tempCount

		for i in range(35):
			if(row[35] == 'D1'):
				probD1 *= (D1[i][row[i]]-1)/tempD1Count if row[i] in D1[i] else 0
				probD2 *= (D2[i][row[i]])/tempD2Count if row[i] in D2[i] else 0
				probD3 *= (D3[i][row[i]])/tempD3Count if row[i] in D3[i] else 0
				probD4 *= (D4[i][row[i]])/tempD4Count if row[i] in D4[i] else 0

			elif(row[35] == 'D2'):
				probD1 *= (D1[i][row[i]])/tempD1Count if row[i] in D1[i] else 0
				probD2 *= (D2[i][row[i]]-1)/tempD2Count if row[i] in D2[i] else 0
				probD3 *= (D3[i][row[i]])/tempD3Count if row[i] in D3[i] else 0
				probD4 *= (D4[i][row[i]])/tempD4Count if row[i] in D4[i] else 0

			elif(row[35] == 'D3'):
				probD1 *= (D1[i][row[i]])/tempD1Count if row[i] in D1[i] else 0
				probD2 *= (D2[i][row[i]])/tempD2Count if row[i] in D2[i] else 0
				probD3 *= (D3[i][row[i]]-1)/tempD3Count if row[i] in D3[i] else 0
				probD4 *= (D4[i][row[i]])/tempD4Count if row[i] in D4[i] else 0

			elif(row[35] == 'D4'):
				probD1 *= (D1[i][row[i]])/tempD1Count if row[i] in D1[i] else 0
				probD2 *= (D2[i][row[i]])/tempD2Count if row[i] in D2[i] else 0
				probD3 *= (D3[i][row[i]])/tempD3Count if row[i] in D3[i] else 0
				probD4 *= (D4[i][row[i]]-1)/tempD4Count if row[i] in D4[i] else 0

		if(probD1 == probD2 == probD3 == probD4):
			continue

		probabilities = {'D1':probD1, 'D2':probD2, 'D3':probD3, 'D4':probD4}
		
		if(row[35] == max(probabilities.items(), key=operator.itemgetter(1))[0]):
			rightPrediction += 1

accuracy = round(rightPrediction/count, 7) * 100

with open('result','w') as output:
	output.write(str(accuracy))