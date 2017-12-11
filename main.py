import os
import subprocess
import csv
import json 
# Termux Cell Heatmapper
# by wisemonkey
# 20171205
# main.py program for outputing the location and signal strangth to a file

file = open("ouput.txt")

get_signal_strength_command = "dir ."
#https://stackoverflow.com/questions/20140137/passing-variables-to-subprocess-popen
signal_strength_json = os.popen(get_signal_strength_command).read()

print(signal_strength_json)


# #http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# #https://stackoverflow.com/questions/11151719/python-writerows-trouble
# with open('data.csv', 'w') as file:
# 	csv_file = csv.writer(file)
# 	test = json.loads('"asdf","asd"')
# 	print(test)
# 	csv_file.writerow(csv) #todo get json to here in [loc, dbm]

file.write(signal_strength_json)

file.close()

