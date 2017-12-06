import os
import subprocess
import csv
# Termux Cell Heatmapper
# by wisemonkey
# 20171205
# main.py program for outputing the location and signal strangth to a file

get_signal_strength_command = "dir ."
#https://stackoverflow.com/questions/20140137/passing-variables-to-subprocess-popen
signal_strength_json = os.popen(get_signal_strength_command).read()

print(signal_strength_json)

with open('data.csv', 'w') as file:
	csv_file = csv.writer(file)
	csv_file.writerow(["asdf","asd"]) #todo get json to here in [loc, dbm]
