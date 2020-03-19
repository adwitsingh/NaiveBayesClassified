# P&S Assignment 3
# Name: ADWIT SINGH KOCHAR
# Roll Number: 2018276
# Section: A
# Group: 8

"""
	Calculates accuracy for Shuttle Landing Control Dataset
"""
import csv

noauto = [{'1':0,'2':0,'3':0,'4':0,'*':0} for x in range(7)]							# Caluclated Constants
auto = [{'1':0,'2':0,'3':0,'4':0,'*':0} for x in range(7)]
count = 0
rightPrediction = 0
autoCount = 0
noautoCount = 0

with open('shuttle-landing-control.data') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	for row in csv_reader:														# TRAINING
		count += 1
		if(row[0] == '1'):
			noautoCount += 1
			for i in range(1,7):
				noauto[i][row[i]] +=1
		else:
			autoCount += 1
			for i in range(1,7):
				auto[i][row[i]] +=1

	csv_file.seek(0)

	for row in csv_reader:														# TESTING
		tempCount = count - 1
		tempAutoCount = autoCount if row[0] != '2' else autoCount-1
		tempNoAutoCount = noautoCount if row[0] != '1' else noautoCount-1

		probAuto = tempAutoCount/tempCount
		probNoAuto = tempNoAutoCount/tempCount

		for i in range(1,7):											# Also adds the Don't Cares
			if(row[0] == '1'):
				probNoAuto *= (noauto[i][row[i]]-1+noauto[i]['*'])/tempNoAutoCount if row[i] != '*' else 1
				probAuto *= (auto[i][row[i]]+auto[i]['*'])/tempAutoCount if row[i] != '*' else 1
			else:
				probNoAuto *= (noauto[i][row[i]]+noauto[i]['*'])/tempNoAutoCount if row[i] != '*' else 1
				probAuto *= (auto[i][row[i]]-1+auto[i]['*'])/tempAutoCount if row[i] != '*' else 1

		if(probAuto > probNoAuto):
			if(row[0] == '2'):
				rightPrediction+=1
		elif(probNoAuto > probAuto):
			if(row[0] == '1'):
				rightPrediction+=1 

accuracy = round(rightPrediction/count, 7) * 100

with open('result','w') as output:
	output.write(str(accuracy))