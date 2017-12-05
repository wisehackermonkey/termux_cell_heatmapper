import os
import subprocess
# Termux Cell Heatmapper
# by wisemonkey
# 20171205
# main.py program for outputing the location and signal strangth to a file

get_signal_strength_command = "dir ."
signal_strength_json = os.popen(get_signal_strength_command).read()

print(signal_strength_json)