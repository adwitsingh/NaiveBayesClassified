# P&S Assignment 3
# Name: ADWIT SINGH KOCHAR
# Roll Number: 2018276
# Section: A
# Group: 8

"""
	Used to combine the accuracy results into the final file.
"""
import csv
import pandas as pd
import os

files = ['Tic-Tac-Toe Endgame', 'SPECT Heart', 'Soybean (Small)', 'Shuttle Landing Control', "MONK's Problems"]

with open('Final Results.csv', mode='w') as output_file:
	output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	output_writer.writerow(['Datasets','Accuracy %'])
	for name in files:
		with open(name + "/result") as accuracy_file:
			if(name != "MONK's Problems"):
				accuracy = accuracy_file.readline()
				output_writer.writerow([name + " Data Set", accuracy])
			else:
				flavor = ['(1)', '(2)', '(3)', '(Combined)']
				for i in flavor:
					accuracy = accuracy_file.readline()
					output_writer.writerow([name + " Data Set " + i, accuracy])

####### Converting to xls ##############
data = pd.read_csv("Final Results.csv", sep=',')
excel_writer = pd.ExcelWriter("./Final Results.xlsx", engine='xlsxwriter')
data.to_excel(excel_writer, index=False)
excel_writer.save()

if os.path.exists("Final Results.csv"):
  os.remove("Final Results.csv")