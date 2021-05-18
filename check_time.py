import urllib.request as u
import sys, requests
import datetime
import os

today = datetime.datetime.now()
available = {}

#Line message stuff
LINE_TOKEN = "Nx2jv18q15UHfNK6g3ucK7zEOAWZk8D4GQQqaUXY85O"
#LINE_TOKEN = "NZhc3XwoWWyF9EuxAZi05SbFCCFo8PHbXNWC2tawH2Z"

for i in range(60):
	day = today + datetime.timedelta(days=i)
	text = str(day.year) + "-" + str(day.month) + "-" + str(day.day)
	query = "http://api.eztable.com/v3/hotpot/quota/" + text + "?restaurant_id=14039&people=5"

	data = requests.get(query).json()
	for j in data['available_people']:
		if available.has_key(text):
			available[text] = available[text].append(j)
		else:
			available[text] = [j]

if available:
	message = available
	os.system("curl -X POST -H 'Authorization: Bearer {0}' -F 'message={1}' https://notify-api.line.me/api/notify".format(LINE_TOKEN, message))
