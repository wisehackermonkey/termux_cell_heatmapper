import os
import json
import csv
#todo https://docs.python.org/3.5/library/datetime.html#module-datetime

shell_command_get_gps_location = "type json.json.txt"#"termux-location -p gps -r once"
shell_command_get_cell_signstrength = "type json.json.txt"#"termux-telephony-cellinfo"




with open('heatmap.csv', 'a+') as csvfile:
	heatmap = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

	location = ''
	signal = ''
	with os.popen(shell_command_get_gps_location) as location_json:
		location = json.loads(location_json.read())
		print(location)

	with os.popen(shell_command_get_cell_signstrength) as signal_json:
		signal = json.loads(signal_json.read())
		print(signal)

	heatmap.writerow([location["id"]] + [signal["id"]])
