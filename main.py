import os
import subprocess
# Termux Cell Heatmapper
# by wisemonkey
# 20171205
# main.py program for outputing the location and signal strangth to a file

file = open("ouput.txt")

get_signal_strength_command = "dir ."
#https://stackoverflow.com/questions/20140137/passing-variables-to-subprocess-popen
signal_strength_json = os.popen(get_signal_strength_command).read()

print(signal_strength_json)

file.write(signal_strength_json)

file.close()


